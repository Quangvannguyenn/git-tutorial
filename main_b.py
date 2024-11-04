data = dict()

with open("f.txt", "r") as f:
    for line in f.readlines():
        data[line] = 1
        

for key in data.keys():
    print(key)