list1 = [100, 35, 23, 100, 45, 89, 90] 
counta100 = list1.count(100) 
counta90 = list1.count(90) 
if counta100 == 2 and counta90 >=2:
  print(f"\nIn List-1:\n -> 100 occured {counta100} times & 90 - {counta90} times.\nThus, Condition is satisfied.") 
else: 
  print(f"\nIn List-1:\n -> 100 occured {counta100} times & 90 only {counta90} time.\nThus, Condition is unsatisfied.")

list2 = [90, 110, 130, 150, 170, 200, 200] 
counta200 = list2.count(200) 
counta130 = list2.count(130) 
if counta200 >= 2 and counta130 == 1: 
  print(f"\nIn List-2:\n -> 200 occured {counta200} times & 130 only {counta130} time.\nThus, Condition is satisfied.") 
else:
  print(f"\nIn List-2:\n -> 200 occured {counta200} times & 130 - {counta130} times. Thus, Condition is unsatisfied.")

