import requests

def get_html(url):
    print('324asfdasf')
    r = requests.get(url)
    return r.text

print("hi")