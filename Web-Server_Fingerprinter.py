import requests

def get_webserver_fingerprint(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            server_header = response.headers.get('Server')
            if server_header:
                return server_header
            else:
                return "Web server fingerprint not found."
        else:
            return f"Failed to retrieve response from {url}. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Failed to connect to {url}: {e}"
url = input("Enter URL of the web server to fingerprint: ")
fingerprint = get_webserver_fingerprint("http://"+url)
print("Web server fingerprint: ", fingerprint)