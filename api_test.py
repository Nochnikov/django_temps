import requests

url = 'http://localhost:8000/posts/'

response = requests.post(url, json={'title': 'DRF intro',
                                    'content': 'dssdsd',
                                    'author': 1
                                    })
# response = requests.post(url, json={'title': 'DRF intro'})
# response = requests.get(url, params={'post_id': 5})


print(response.headers)
print(response.text)