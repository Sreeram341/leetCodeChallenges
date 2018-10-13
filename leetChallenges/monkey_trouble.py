def monkey_trouble(a_smile, b_smile):
  if (a_smile == False and b_smile == False) or (a_smile== True and b_smile == True):
      return False
  else:
      return True
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))