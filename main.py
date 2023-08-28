import requests
import json

print("\nWelcome to Adil SubFinder\n")
domain = input("Enter Domain Name: ")
N = input("\nCheck Only Numbers? ")
print(N)

def finder(d, num):
    import requests

    url = f"https://api.securitytrails.com/v1/domain/{d}/subdomains"

    headers = {
    "accept": "application/json",
    "APIKEY": "{{Your_Api_Key_Here}}"
    }

    response = requests.get(url, headers=headers)

    res = json.loads(response.text)
    subdomains = res["subdomains"]
    suffix = f"{d}"


    if num == "n":

        # Print the list of subdomains with the prefix
        for subdomain in subdomains:
            full_subdomain = f"{subdomain}.{suffix}"
            print(full_subdomain)   
    else:
        print(f"\nTotal {len(subdomains)} Found..!")


finder(domain, N)
