list = (input('\nEnter the Elements for the List: \n').split()) 
a = len(list)
b = list[2]
print('\n> Final List: ', list)
print('\n> Length of Entered List: ', a)
print('\n> The 3rd Element in the List: ', b)

if a > 10 and list.count(list[2])>1:
  print('\nTRUE')
else:
  print('\nFALSE')
