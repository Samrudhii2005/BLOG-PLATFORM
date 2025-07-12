import requests


register_url = "http://127.0.0.1:8000/api/register/"
new_user = {
    "username": "bob",
    "password": "bob@123"
}

register_response = requests.post(register_url, json=new_user)
print("Registration Status:", register_response.status_code)
print("Registration Response:", register_response.text)


login_url = "http://127.0.0.1:8000/api/login/"
credentials = {
    "username": "samrudhi",
    "password": "samrudhi@2005"
}

response = requests.post(login_url, json=credentials)
print("Login Status:", response.status_code)
print("Login Response:", response.text)

tokens = response.json()
access_token = tokens['access_token']
refresh_token = tokens['refresh_token']


blogs_url = "http://127.0.0.1:8000/api/blogs/"
headers = {'Authorization': f'Bearer {access_token}'}

blog_response = requests.get(blogs_url, headers=headers)
print("\nInitial Blog Response:", blog_response.json())



create_blog_url = "http://127.0.0.1:8000/api/blogs/"
blog_headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
blog_data = {
    "title": "My Second Blog",
    "content": "hey this is my second vlog!"
}

create_response = requests.post(create_blog_url, headers=blog_headers, json=blog_data)
print("\nBlog Creation Status:", create_response.status_code)
print("Blog Creation Response:", create_response.text)


comment_url = "http://127.0.0.1:8000/api/comments/"
comment_headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
comment_data = {
    "blog": 1,  
    "text": "good workk!"
}

comment_response = requests.post(comment_url, headers=comment_headers, json=comment_data)
print("\nComment Creation Status:", comment_response.status_code)
print("Comment Creation Response:", comment_response.text)

