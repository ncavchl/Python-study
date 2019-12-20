f=open("read.txt", "r")
s=f.readline()
#print(f.read())
#print("ㅋㅋ")
print(s, len(s))
#print(s.split("\n"))
#print(s.strip())
#print(s)

#for l in f:
#    s=l.strip()
#
#print(s, end=" ")
#list = f.readlines()
#print(list) #개행문자포함

planets = []
for line in f:
    planets.append(line.strip())

print(planets)
f.close()