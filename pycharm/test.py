f=open("read.txt","r")
for line in f:
    word=line.strip()
    if len(word) > 9:
        print(word)
f.close()