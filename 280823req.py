import requests
import pprint
# params={"q":"aert"}
# response=requests.get("https://www.google.com/search",params=params)
# print(response.status_code)
# print(response.headers)
# print(response.text)
response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
pprint.pprint(json_response)
print(json_response['data'])
print(json_response['headers']['Content-Type'])


def f():
    pass