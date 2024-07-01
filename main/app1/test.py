import requests

import requests


url = 'https://joshya1234.pythonanywhere.com/api/Employee/30/'


data = {
    'name': 'Joshya12435',
    'salary': '5',
    'age': '20',
    'image': 'https://media.proglib.io/posts/2021/02/26/d13690e6ee2380bbc4abe200d9d4fcdb.webp'
}


response = requests.patch(url, data=data)


print(response.json())

response = requests.get('https://joshya1234.pythonanywhere.com/api/Employee/?format=json')
print(response.text)

