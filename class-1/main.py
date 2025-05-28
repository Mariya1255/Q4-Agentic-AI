import requests

def main():
    response = requests.get("https://www.asharib.xyz/api/profile")
    print(response.json())


if __name__ == "__main__":
    main()
