import requests
import pprint

BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products")
pprint.pprint(response.json())