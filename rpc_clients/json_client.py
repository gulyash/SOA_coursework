from jsonrpcclient import request
response = request("http://localhost:8000/rpc/", "urls")
for url in response.data.result:
    print(url)

new_token = request("http://localhost:8000/rpc/", "get_token", "https://github.com/gulyash")
print(new_token.data.result)
