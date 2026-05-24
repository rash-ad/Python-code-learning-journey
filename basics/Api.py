import requests
response = requests.get('https://fakestoreapi.com/products/1')

for i in range(1, 6):
    response = requests.get(f'https://fakestoreapi.com/products/{i}')
    print(response.json())
response = requests.get('https://fakestoreapi.com/products')
print("Products: " + str(response.json()))