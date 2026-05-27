# datas={
#     "person1":{
#         "name":"Vetri",
#         "phone":"98745663210"
#     },
#     "person2":{
#         "name":"Dharshan",
#         "phone":"98745663210"
#     }
# }

# print(datas["person1"]["name"])

carAttributes={"name":"mustang","year":2005}
carAttributes["color"]="black"

d={"Fuel":"Petrol"}

carAttributes.update(d)

for x in carAttributes:
    print(x,carAttributes[x])