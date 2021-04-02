users = [
 { "id": 0, "name": "Hero" },
 { "id": 1, "name": "Dunn" },
 { "id": 2, "name": "Sue" },
 { "id": 3, "name": "Chi" },
 { "id": 4, "name": "Thor" },
 { "id": 5, "name": "Clive" },
 { "id": 6, "name": "Hicks" },
 { "id": 7, "name": "Devin" },
 { "id": 8, "name": "Kate" },
 { "id": 9, "name": "Klein" }
]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []
    # print(user)


for i, j in friendships:
    users[i]["friends"].append(j)
    users[j]["friends"].append(i)

for user in users:
    print(user)





def number_of_friends(user):
 return len(user["friends"])

num_list = []
for user in users:
    num_list.append(number_of_friends(user))
    print(num_list)

    print([number_of_friends(user)for user in users])

mean = sum(num_list)/len(num_list)
print(mean)


#  total_connections = sum(number_of_friends(user
#
#
#  for user in users)# def number_of_friends(user):
#
#
# #  """how many friends does _user_ have?"""
# #  return len(user["friends"]) # length of friend_ids list
# # total_connections = sum(number_of_friends(user)
# #  for user in users) # 24
#













