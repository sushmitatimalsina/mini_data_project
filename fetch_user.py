import requests
import pandas as pd

# users_url = "https://jsonplaceholder.typicode.com/users"
# users_data = requests.get(users_url).json()

# users = []
# for u in users_data:
#     users.append({
#         "ID": u["id"],
#         "Name": u["name"],
#         "Username": u["username"],
#         "Email": u["email"],
#         "City": u["address"]["city"]
#     })
# df_users = pd.DataFrame(users)
# df_users.to_excel("users.xlsx", index=False)
# print("Users saved to users.xlsx")   

post_url = "https://jsonplaceholder.typicode.com/posts"
post_data = requests.get(post_url).json()

posts = []
for p in post_data:
    posts.append({
        "PostID": p["id"],
        "UserID": p["userId"],
        "Title": p["title"],
        "Body": p["body"]
    })
df_posts = pd.DataFrame(posts)
df_posts.to_excel("posts.xlsx", index=False)
print("Posts saved to posts.xlsx")

todos_url = "https://jsonplaceholder.typicode.com/todos"
todos_data = requests.get(todos_url).json()

todos = []
for t in todos_data:
    if not t["completed"]:
        todos.append({
            "TodoID": t["id"],
            "UserID": t["userId"],
            "Title": t["title"],
            "Completed": t["completed"]
        })

df_todos = pd.DataFrame(todos)
df_todos.to_excel("todos.xlsx", index=False)
print("Todos saved to todos.xlsx (only incomplete todos)")