list = [] 

response_size = int(input('Size of the list'))

for x in range (0,response_size,1):
  response_int = int(input('Please input a number'))
  list.append(response_int)

print('TASK 1. Current list is: ' + str(list))

list[0] = 99

print ('TASK 2. ' + str(list))

list[0] = 100

print ('TASK 3. ' + str(list))

list_2 = [500,600,700,800,900]
print('TASK 4_1. ' + str(list_2))

list.extend(list_2)
print('TASK 4_2. ' + str(list))

list.remove(800)
print('TASK 5. ' + str(list))

list.remove(list[2])
print('TASK 6. ' + str(list))

grades = ["A", "B", "C", "A", "A", "C"]
print('TASK 7. ' + str(grades))
count = 0
for x in grades:
  if(x=="A"):
    count=count+1

print('TASK 8. Count of the number of A grades ' + str(count))

print('TASK 9. Position of B is : ' + str(grades.index("B")))

exists_f = False
for x in grades:
  if(x=="F"):
    exists_f = True
if(exists_f==False):
  print('TASK 10. "F" grade doesnt exist')

list_2.clear()
print('TASK 11. After clear ' + str(list_2))

del list_2

print('TASK 12. GAVE ERROR PLEASE CHECK CODE')

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print('TASK 13. names: ' + str(players))

players.sort()
print('TASK 14. sorted names: ' + str(players))

players2 = players.copy()
print('TASK 15. players2: ' + str(players2))

players2.sort(reverse=True)
print('TASK 16. players: ' + str(players) + 
      '\n         players2: ' + str(players2))
