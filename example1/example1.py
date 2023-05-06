import io

f = open("input.txt", "r")
header = f.readline()
print(header.split(","))

max_no = 0
name = ""

for line in f.readlines():
    data = line.split(",")
    data[1] = int(data[1])
    data = tuple(data)
    if max_no < data[1]:
        max_no = data[1]
        name = data[0]

f.close()
print("Elevul cu cele mai multe absente este %s si are %d absente" % (name, max_no))