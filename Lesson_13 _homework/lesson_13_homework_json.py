import requests
from pprint import pprint
import json
import csv

URL = 'https://jsonplaceholder.typicode.com/users'
URL2 = 'https://jsonplaceholder.typicode.com/posts'
URL3 = 'https://jsonplaceholder.typicode.com/comments'
URL4 = 'https://jsonplaceholder.typicode.com/albums'
URL5 = 'https://jsonplaceholder.typicode.com/photos'
URL6 = 'https://jsonplaceholder.typicode.com/todos'
users = requests.get(URL).json()
posts = requests.get(URL2).json()
comments = requests.get(URL3).json()
albums = requests.get(URL4).json()
photos = requests.get(URL5).json()
todos = requests.get(URL6).json()

with open('users_import.json', mode='w', encoding='UTF-8') as file:
     json.dump(users, file, ensure_ascii=False, indent=4)
with open('posts_import.json', mode='w', encoding='UTF-8') as file:
     json.dump(posts, file, ensure_ascii=False, indent=4)
with open('comments_import.json', mode='w', encoding='UTF-8') as file:
     json.dump(comments, file, ensure_ascii=False, indent=4)
with open('albums_import.json', mode='w', encoding='UTF-8') as file:
     json.dump(albums, file, ensure_ascii=False, indent=4)
with open('photos_import.json', mode='w', encoding='UTF-8') as file:
     json.dump(photos, file, ensure_ascii=False, indent=4)
with open('todos_import.json', mode='w', encoding='UTF-8') as file:
     json.dump(todos, file, ensure_ascii=False, indent=4)

users_headers = users[0].keys()
for user in users:
    with open('users_data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=users_headers)
        writer.writeheader()
        for user in users:
            writer.writerow(user)

posts_headers = posts[0].keys()
for post in posts:
    with open('posts_data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=posts_headers)
        writer.writeheader()
        for post in posts:
            writer.writerow(post)

comments_headers = comments[0].keys()
for comment in comments:
    with open('comments_data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=comments_headers)
        writer.writeheader()
        for comment in comments:
            writer.writerow(comment)

albums_headers = albums[0].keys()
for album in albums:
    with open('albums_data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=albums_headers)
        writer.writeheader()
        for album in albums:
            writer.writerow(album)

photos_headers = photos[0].keys()
for photo in photos:
    with open('photos_data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=photos_headers)
        writer.writeheader()
        for photo in photos:
            writer.writerow(photo)

todos_headers = todos[0].keys()
for todo in todos:
    with open('todos_data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=todos_headers)
        writer.writeheader()
        for todo in todos:
            writer.writerow(todo)

users2 = []
with open('users_data.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        users2.append(line)
with open('from_csv_users_data.json', mode='w', encoding='UTF-8') as file:
    json.dump(users2, file, ensure_ascii=False, indent=4)

posts2 = []
with open('posts_data.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        posts2.append(line)
with open('from_csv_posts_data.json', mode='w', encoding='UTF-8') as file:
    json.dump(posts2, file, ensure_ascii=False, indent=4)

comments2 = []
with open('comments_data.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        comments2.append(line)
with open('from_csv_comments_data.json', mode='w', encoding='UTF-8') as file:
    json.dump(comments2, file, ensure_ascii=False, indent=4)

albums2 = []
with open('albums_data.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        albums2.append(line)
with open('from_csv_albums_data.json', mode='w', encoding='UTF-8') as file:
    json.dump(albums2, file, ensure_ascii=False, indent=4)

photos2 = []
with open('photos_data.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        photos2.append(line)
with open('from_csv_photos_data.json', mode='w', encoding='UTF-8') as file:
    json.dump(photos2, file, ensure_ascii=False, indent=4)

todos2 = []
with open('todos_data.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        todos2.append(line)
with open('from_csv_todos_data.json', mode='w', encoding='UTF-8') as file:
    json.dump(todos2, file, ensure_ascii=False, indent=4)
