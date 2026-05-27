# inputs=[int(x) for x in input("Enter the elements : ").split(" ")]
#inputs=list(map(int,input("Enter elements space seperated : ").split()))

# inputs=[x**2 for x in range(1,10+1) if(x%2==0)]
# print(inputs)

productList=list()

for i in range(2):

    product=list()

    id=int(input("Enter id : "))
    product.append(id)

    name=input("Enter product name : ")
    product.append(name)

    price=float(input("Enter Price : "))
    product.append(price)

    productList.append(product)

    
print(productList)
