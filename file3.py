import requests

def get_html(url):
    print("file3 program")
    r = requests.get(url)
    return r.text

print("hi")