import os
import random
import config

def study_from_created_set():
  while True:
    flashOrTest = config.error_control('f', 't', '\nTo study flashcard style, type \'F\'. To test yourself, type \'T\': ')
    orderOrRandom = config.error_control('o', 'r', 'Would you like the flashcards to presented in order (\'O\') or randomly (\'R\')? ')
    if flashOrTest == True:
      termOrDef = config.error_control('t', 'd', 'Would you like the term first (\'T\') or definition first (\'D\')? ')
    elif flashOrTest == False:
      termOrDef = config.error_control('t', 'd', 'Would you like to input the term (\'T\') or the definition (\'D\')? ')
    
    with open(config.workingFolder + r'/' + workingSet, 'r') as file:
      lineList = file.readlines()
      lenLineList = len(lineList)

      for indece in range(0, lenLineList):
        if orderOrRandom == True:
          tempFlashcard = lineList[indece]
        elif orderOrRandom == False:
          tempFlashcard = random.choice(lineList)
          lineList.remove(tempFlashcard)
        tempFlashcard = tempFlashcard.rstrip('\n').split(chr(0x2588))

        term = tempFlashcard[0]
        definition = tempFlashcard[1]

        if termOrDef == True:
          outputFormat = {'choice1':'term', 'choice2':'definition', 'var1':term,'var2':definition}
        elif termOrDef == False:
          outputFormat = {'choice1':'definition', 'choice2':'term', 'var1':definition,'var2':term}

        if flashOrTest  == True:
          flashcard_style(outputFormat, indece, lenLineList)
        elif flashOrTest == False:
          test_yourself(outputFormat, indece)
    
    if config.error_control('yes', 'no', '\nWould you like to study this set again? (Enter Yes or No) ') != True:
      break

def flashcard_style(outputFormat, indece, lenLineList):
  print(('\n{} {}: {}').format(outputFormat['choice1'], str(indece+1), outputFormat['var1']))
  input('\nPress enter when you are ready for the {}: '.format(outputFormat['choice2']))
  print(('\n{} {}: {}').format(outputFormat['choice2'], str(indece+1), outputFormat['var2']))
  if (indece+1) < lenLineList:
    input('\nPress enter when you are ready for the next {}: '.format(outputFormat['choice1']))

def test_yourself(outputFormat, indece):
  guessAgain = 'y'
  while guessAgain == 'y':
    print(('\n{} {}: {}').format(outputFormat['choice2'], str(indece+1), outputFormat['var2']))
    guess = input(('Type in the correct {} for {} {}: ').format(outputFormat['choice1'], outputFormat['choice2'], str(indece+1)))
    if guess == outputFormat['var1'].strip():
      input('You got the {} right! Press enter to continue.'.format(outputFormat['choice2']))
      break
    guessAgain = input('Your guess did not match the correct {}. Would you like to try again? '.format(outputFormat['choice1']))
    if guessAgain[0].lower() == 'y':
      guessAgain = 'y'
    else:
      input(('The correct {} to {} {} is {}. Press enter to continue').format(outputFormat['choice2'], outputFormat['choice1'], str(indece+1), outputFormat['var1']))

def main():
  while True:
    choiceList = os.listdir(config.workingFolder)
    choiceList.sort()
    
    try:
      os.remove(config.workingFolder + r'/.DS_Store')
    except:
      pass

    setChoice = input('\nEnter the number of the set you would like to study from. If you only have 1 set, enter (1). If you would not like to study from a created set, enter \'No\' ')
    if setChoice.lower() == 'no':
      return
    try:
      setChoice = int(setChoice)-1
      for indece in range(0, len(choiceList)):
        if (setChoice) == indece:
          global workingSet
          workingSet = choiceList[setChoice]
          study_from_created_set()
          return
      else:
        print('Please enter a number between 1 and {} '.format(len(choiceList)))
    except:
      print('Please enter a number between 1 and {}'.format(len(choiceList)))

if __name__ == '__main__':
  main()
