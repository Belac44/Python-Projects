facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Commments": 2, "Shares": 1},
    {"Likes": 33, "Commments": 8, "Shares": 3},
{"Shares": 2, "Comments": 4},
{"Shares": 1, "Comments": 1},
{"Likes": 19, "Comments": 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass

print(total_likes)