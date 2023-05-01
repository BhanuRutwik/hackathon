import requests

def get_html(url):
    r = requests.get(url)
    print('go to hell and heaven')
    return r.text

print("hi")