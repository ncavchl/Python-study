f=open("read.txt", "r")
current = 0
apple = 0
for line in f:
    current+=1
    planet = line.strip().lower()
    if planet == "apple":
        apple = current

print("Apple is line #%d" %apple)