print("hello")

void = ""

field = []


voids = []

for i in range(8):
  voids.append(void)

axis = []
axis.append(void)
axis.extend(list(range(1,10)))
field.append(axis)

print(axis)

for i in range(1,10):
  column = []
  column.append(i)
  field.append(column)

for column in field:
  for number in column:
    print(number, end=" ")
  print(end= "\n")
  

print()
"""
axis = list(range(9))

for n in axis:
  for n in axis:
    print(n,end=" ")
  print(end ="\n")

print()

for i in range(9):
  for j in range(9):
    print(list(range(9)),end="")
  print(end= "\n")
"""