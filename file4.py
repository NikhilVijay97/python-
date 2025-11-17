filename = "bbb.txt"

with open(filename, "r") as file:
    lines = file.read().splitlines()

print(lines)
