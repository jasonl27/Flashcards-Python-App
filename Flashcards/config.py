workingFolder = ''

#Error Control Function - logic1 and logic2 are error control breakers
def error_control(logic1, logic2, text):
  errorControl = True
  while errorControl == True:
    userInput = input(text).lower()
    if userInput == logic1:
      return True
    elif userInput == logic2:
      return False
    else:
      print('Please answer {} or {}'.format(logic1, logic2))