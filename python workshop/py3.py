Student1="Dhanu"
Student2="Raam"
Student3="Seetha"
Student4='Jashvik'
student_names=["Dhanu","Raam","seetha","Jashvik"]
print(student_names)
print("---------")
print(student_names[1])
print("---------")
student_names[3]="Rosie"
print(student_names[3])

print("---------")
student_names.append("shivu")
print(f" added shivu:{student_names}")

print("---------")
student_names.append("Raaj")
print(f" added Raaj{student_names}")

print("---------")
student_names.append("Lilly")
print(f"added lilly {student_names}")

print("---------")
student_names.append("Dolly")
print(f"{student_names}")
print("---------")

student_names.remove("shivu")
print(f"{student_names}")
print("---------")
student_names.remove("Dolly")
print(f"{student_names}")
print("---------")
student_names.insert(2,"Mona")
print(student_names)
print("---------")
student_names.insert(3,"yash")
print(student_names)
print("---------")
student_names.insert(5,"sandyy")
print(student_names)
print("---------")
student_names.pop(3)
print(f"{student_names}")
print("---------")
print(f"length of list:{len(student_names)}")
print("---------")
print(student_names.reverse())
print("---------")
print(type(student_names))































