import requests
import sys
from bs4 import BeautifulSoup

#idea is to extract all form of URLs you can get from a single HTTP request's resposne, to identify other sources of URLs interacting with it.
def urlscraping(url):

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')


    # <a href=""> tags are first step of extracting all the URLs in an endpoint!
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

    # TODO: where else can we find URL/endpoints from a single HTTP reponse? maybe indirect text references with "https://" specified?



   


urlscraping(sys.argv[1])


