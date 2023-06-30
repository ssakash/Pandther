import sys
import requests
from bs4 import BeautifulSoup
import urllib.parse

def print_title():
     print("="*50)
     print("               Pandther                   ")
     print("="*50)
     print("\n\n")

def print_header(x):
    print("="*50)
    print(f"Operations to perform on ({x})")
    print("="*50)
    print("1/ Display links in endpoint")
    print("2/ Links")
    print("="*50)

# List of all reference list in the provided URL
def fetch_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        return 'Failed to get the webpage.'

    web_content = response.text
    soup = BeautifulSoup(web_content, 'html.parser')

    links = soup.find_all('a')
    url_list = []

    for link in links:
        href = link.get('href')
        if href:
            parsed = urllib.parse.urljoin(url, href)
            url_list.append(parsed)

    return url_list


#The main input in our script is primarily an endpoint. (https://endpoint.com) and we do all processing in it.
endpoint = sys.argv[1]

print_title()
selection = "c"
while (selection != 'q' and selection != 'Q'):
    print_header(endpoint)

    selection = input("Your choice? (Press Q to quit)")
    if( selection == "1"):
        links = fetch_links(endpoint)
        print("Links present in the endpoint are:")
        for i in links:
            print(i)