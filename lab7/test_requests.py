import requests

def main():

    print("hello world")

    url = "https://httpbin.org/get"

    resp = requests.get(url)

    print(resp.status_code)

main()