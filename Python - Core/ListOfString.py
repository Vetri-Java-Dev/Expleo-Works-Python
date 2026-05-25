products=input("Enter products seperated by comma : ")
productList=products.split(",")

print("Products : ")
for i in range(len(productList)):
    print(productList[i])