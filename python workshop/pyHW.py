
product=["smartphone","laptop","keyboard","notebook","bike","watch","headphone"]
print(product)
print(len(product))
print("------")
product.append("speaker")
print(f" added speaker : {product}")
print("------")
product.append("pen")
print(f" added pen : {product}")
print("------")
product.append("bag")
print(f"added bag :{product}")
print("------")
print(len(product))
print("------")
product.remove("speaker")
print(f" removed speaker : {product}")
print("------")
product.remove("bike")
print(f" removed bike : {product}")
print("------")
product.remove("laptop")
print(f" removed laptop : {product}")
print("------")
print(len(product))
print("------")
product.remove("watch")
print(f" removed watch: {product}")
print("------")
print(len(product))
product.pop(2)
print(f"{product}")
print("---  dict---")

data={"name":"anu","age":20,"course":"MCA","college":"JNNCE"}
print(data)
print("------")

data["age"]=25
print(data)
print("------")

print(data.values())
print(data.keys())
print("------")


print("------  tuple------")
product=("smartphone","laptop","keyboard","notebook","bike","watch","headphone")
print(product)
print(len(product))

product.append("pen")
print(f" add watch: {product}")
print("------")
product.remove("watch")
print(f" removed watch: {product}")
print("------")

product={"smartphone","laptop","keyboard","notebook","bike","watch","headphone"}



