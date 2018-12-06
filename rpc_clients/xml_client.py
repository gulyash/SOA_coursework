import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/rpc/") as proxy:
    response = proxy.urls()
    for url in response:
        print(url)
    print(proxy.get_token("https://github.com/gulyash"))
