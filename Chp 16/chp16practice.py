file = open("super_villains.txt")

for line in file:
    line = line.strip()
    print(line)

file.close()