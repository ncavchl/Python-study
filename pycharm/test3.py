f = open("read.txt", "r")
apple = 0
for line in f:
    planet = line.strip().lower()
    if planet[0] == "#":
        continue
    apple+=1
    if planet == "apple":
        break
print("Apple is line #%d" %apple)
