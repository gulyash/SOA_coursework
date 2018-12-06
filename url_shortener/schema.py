import graphene
from graphene import Node, ObjectType, Schema
from graphene_django import DjangoObjectType, DjangoConnectionField

from url_shortener.models import Url
from url_shortener.tokenizer import Tokenizer

# create token query example:
get_token = """
mutation myFirstMutation {
    getToken(url:"https://pypi.org/project/graphene/") {
        token
    }
}
"""
# get all urls query example:
all_urls = """
query{
  urls{
    edges{
      node{
        token
        creationTime
        redirectCount
      }
    }
  }
}
"""


class UrlNode(DjangoObjectType):
    class Meta:
        model = Url
        interfaces = (Node,)


class Query(ObjectType):
    url = Node.Field(UrlNode)
    urls = DjangoConnectionField(UrlNode)
    token = graphene.String()
    # person = graphene.Field(Person)


class GetToken(graphene.Mutation):
    class Arguments:
        url = graphene.String()

    token = graphene.String()

    def mutate(self, info, url):
        token = Tokenizer().create_token(url)
        return GetToken(token=token)


class MyMutations(graphene.ObjectType):
    get_token = GetToken.Field()


schema = Schema(query=Query, mutation=MyMutations)
