data = {"name": "Alice", "age": 25, "city": "New York"}

with open("data.txt", "w") as f:
    f.write(str(data))

with open("data.txt", "r") as f:
    content = f.read()
    
print("the content of file:")
print(content)




