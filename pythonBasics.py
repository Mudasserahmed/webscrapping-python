
# # data types in python

# # x = "name" string
# # x = ["a","b","c"] tuple
# # x = range(9)  range
# # x = {"name","john","age"} set
# # x = {"name":"john", "age" : 22} dict
# # x = frozenset({"apple","banana","cherry"})  frozenset
# # x= true
# # x = b"hello" bytes 
# #  x = bytearray(5) bytearray
# # x = memoryview(bytes(5)) memoryview 
# # x= none Nonetype
# name =  input("what is your name?")
# print("hello" + name)

# birth_year = input("what is your birth year?")
# age = 2023 - int(birth_year)
# print("your age is " + str(age))

#some string methods

course = "this is python"
check = input("type a string to check pailendrome: "  )
if check[::-1] == check:
    print("pailendrome string")
else :
    print("not pailendrome")
# print(course.upper())
# print(course.find("p"))
# print(course.replace("x","i am"))
# print("python" in  course)

#arthmetic operation 
x = 10
y = 20
z= x + y * 2
print( x + y)
print(z)