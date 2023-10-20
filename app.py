print("hello")
a = []
with open("demo.txt") as file_obj:
    a = file_obj.readlines()
    a = [ req.replace("\n" , "") for req in a]
print(a)