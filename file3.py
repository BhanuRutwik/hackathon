import requests

def get_html(url):
    r = requests.get(url)
    return r.text

print("HTML content:", get_html("https://www.google.com"))
