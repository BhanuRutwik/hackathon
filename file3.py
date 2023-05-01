import requests

def get_html(url):
    print('324')
    r = requests.get(url)
    return r.text

print("hi")