import requests
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='debug_log.txt',
                    filemode='w')
def load_wordlist(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            wordlist = [line.strip() for line in file]
        return wordlist
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except IOError:
        print(f"Error reading file: {file_path}")
        return []

def send_options_request(url):
    try:
        apis_found = []
        w = load_wordlist("api_wordlist.txt")
        for i in w:
            fuzzurl = url+"/"+ i
            response = requests.options(fuzzurl, timeout=5)
            print(f"Status code: {response.status_code}, URL: {fuzzurl} ", )

            if response.status_code == 200:
                logging.info(response.text)
                if 'Allow' in response.headers:
                    print("Allowed methods: ", response.headers['Allow'])
                    apis_found.append(fuzzurl)
                else:
                    print("No 'Allow' header in the response")

    except requests.RequestException as e:
        print("An error occurred: ", str(e))

    return apis_found

def main():
    if len(sys.argv) != 3:
        print("Commands: ")
        print("1/ python3 Pandther.py recon <url>")
        sys.exit(1)

    action = sys.argv[1]
    url = sys.argv[2]
    
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Invalid URL. Please ensure it starts with 'http://' or 'https://'")
        sys.exit(1)
    if(action == "recon"):
        print(f"Valid APIs found are: {send_options_request(url)}")
    else:
        print(f"Provide valid command. '{action}' isn't one!")

if __name__ == "__main__":
    main()
