import requests

def get_html(url):
    print('324asfd')
    r = requests.get(url)
    return r.text

print("hi")