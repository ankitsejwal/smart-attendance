from flask import Flask, request, json, jsonify
# import attendance

# def read_members():
#     file_path = "/Users/ankitsejwal/Projects/smart-attendance/static/js/members.json"
#     file = open(file_path, "r")
#     members = json.load(file)
#     return members

# members = read_members()

# active_members = members["active_members"]

# data = {
#     "id": 2,
# }

# for member in active_members:
#     if member["id"] == data["id"]:
#         for k, v in member.items():
#             print(v)


list1 = ['mike', 'douglas']
parents = ', '.join(list1)
print(parents)