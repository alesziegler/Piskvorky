print("hello")

field = []

axis = list(range(9))
field.append(axis)

for i in range(9):
  column = []
  column.append(i)
  field.append(column)

extension = ["",'',7]

# what if we extended everything by empty spaces?

field[2].extend(extension)

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