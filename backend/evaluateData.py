import codecs

dataDoc = "backend/bin/data.txt"

lines = [line.strip().split() for line in codecs.open(dataDoc, "r", 'utf-8').readlines()]
print(lines)

# tupel [ , ]
# 