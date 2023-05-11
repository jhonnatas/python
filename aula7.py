try:
  10/0
except (Exception, ZeroDivisionError) as e:
  print(e)
else:
  print('No exception')
finally:
  print('finally')
