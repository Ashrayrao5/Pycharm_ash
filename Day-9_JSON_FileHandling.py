import requests
import pandas as pd
import json

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)


#==============================
# Saving API Data to File(🧪 Save to JSON)
#==============================

# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4)

#************
# indent=4
# Makes file readable.
# Without it → everything on one line.
#*******************



# df = pd.DataFrame(data)
# df.to_csv("posts.csv", index=False)
# print(df.info())
# print(df.describe())

#=====================================================
#How to cleanly open the API only when the API pull is successful
#=====================================================

# if response.status_code == 200:
#     data = response.json()
#     print("Total Posts:",len(data))
#     print("First Post title:", data[0]['title'])
#     print("Last Post ID:", data[-1]['id'])
#
#     user_posts = [post for post in data if post["userId"]== 3]
#
#     print("Total Posts:",len(user_posts))
#
#     print("UserId-3 First 2 Post titles:")
#     for post in user_posts[:2]:
#         print(post['title'])

#=====================================================
# PART 3 — Query Parameters (Server-Side Filtering)
# Instead of downloading everything and filtering locally, we let the API filter.
#=====================================================

# params = {
#     "userId": 5,
#     # "page": 1,
# }
#
# response = requests.get(url, params=params)
#
# if response.status_code == 200:
#     data = response.json()
#     print("Total Posts from API:",len(data))
#     print("First 2 records:", data[:2])
#
# else:
#     print("Error:", response.status_code)

#=====================================================
# PART 4 — Error Handling (Very Important)
# In real pipelines, APIs fail.
#=====================================================

# response = requests.get(url)
#
# if response.status_code == 200:
#     print("Success")
# else:
#     print("Request failed")
#     print("Status code:", response.status_code)


#=====================================================
# PART 5 — Timeout Protection
# If server hangs, your job should not wait forever.
#=====================================================

# try:
#     response = requests.get(
#         "https://jsonplaceholder.typicode.com/posts",
#         timeout=5
#     )
#
#     print("Status:", response.status_code)
#
# except requests.exceptions.Timeout:
#     print("Request timed out")
#
# **************
# Why Timeout Is Critical
# **************
# Imagine:
# Airflow job running
# API freezes
# Job hangs 2 hours
# Timeout prevents this.

#=====================================================
# PART 7 — Flatten Nested JSON
#=====================================================

# if response.status_code == 200:
#     users = response.json()
#     # print(users[:1])
#
#     flattened_users = []
#
#     for user in users:
#         flattened_users.append({
#             "userId": user['userId'],
#             "id": user["id"],
#             "title": user["title"],
#             "body": user["body"],
#         })
#
#     print(flattened_users[:2])




