import requests

def get_html(url):
    r = requests.get(url)
    print('get_html program')
    return r.text

print("hi")