import io
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_axis_off()

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")

grades = []
print(f1.readline().split(","))
print(f2.readline().split(","))

for line in f1.readlines():
    data = line.split(",")
    data[1] = int(data[1])
    grades.append(data[1])

for line in f2.readlines():
    data = line.split(",")
    data[1] = int(data[1])
    grades.append(data[1])

no_of_students = len(grades)
avg_grade = sum(grades) / no_of_students

f1.close()
f2.close()

ax.table(cellText=[[no_of_students, avg_grade]], colLabels=["Numar studenti", "Media notelor"], loc='center')
plt.savefig("table.pdf")
