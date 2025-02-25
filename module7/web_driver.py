import requests

def main():
    print("This is a test for connecting to a website using requests module")
    url = "https://gist.githubusercontent.com/mzakiali/0b78ca62a236a4e3b8db49b0bc58a2ee/raw/a23ec746e8cce7369ce54ded6a7cd1d8f256e94a/parks_neighbourhood_names.txt"
    # if the status code is 200, it means that the connection and response is successful
    try:
        resp = requests.get(url)  # get the response from the website
        list_1 = resp.text.splitlines()
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        return list_1
    
    

if __name__ == "__main__":
    main()