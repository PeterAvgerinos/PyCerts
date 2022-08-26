import json

# data = '''
# {
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }'''

data2 = '''
{
    "name" : ["Peter", "George", "Matt", "Gina", "Carlos"],
    "ID" : {
    "number" : ["1", "2", "3", "4", "5"],
    "letter" : ["P", "G", "M", "G", "C"]
    }
}'''

info = json.loads(data2)
print("Name: ", info["name"][0])
# print("Hide: ", info["ID"]["number"][0]["letter"][0])
