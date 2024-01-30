import codecs

dataDoc = "backend/bin/data/data.txt"

data = [line.strip().split(",") for line in codecs.open(dataDoc, "r", 'utf-8').readlines()]
print(data[0])
print(data[1])

classes = []
[classes.append(data[i][2]) for i in range(1, len(data)) if data[i][2] not in classes]

print(classes)
