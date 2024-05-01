# this is for empty cell:
void = ""
# this is going to be multidimensional array:
field = []
# this is going to be list of empty cells:
voids = []
# this creates list of 8 empty cells:
for i in range(8):
  voids.append(void)
# this is going to be horizontal axis:
horizontal_axis = []
# first cell of horizontal axis is empty:
horizontal_axis.append(void)
# this adds numbers to horizontal axis:
horizontal_axis.extend(list(range(1,10)))
# this ads horizontal axis to the top of playing field:
field.append(horizontal_axis)

for i in range(1,10):
  # this creates 9 rows of playing field:
  row = []
  # this adds vertical axis as a first item of each row:
  row.append(i)
  # this adds 8 empty cells to each row:
  row.extend(voids)
  # this adds rows to a playing field:
  field.append(row)

field[3][4] = 20

for row in field:
  for cell in row:
    # this prints rows, end statement ensures they are printed horizontally:
    print(cell,end=" ")
      # this ensures that next row is printed below previous one>
  print(end= "\n")

field[4][5] = 50

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