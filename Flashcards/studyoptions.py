import os
import random
import config

def study_from_created_set():
  while True:
    while True:
      print('\nWould you like to study flashcard style or test youreslf?') 
      studyChoice = input('To study flashcard style, type \'F\'. To test yourself, type \'T\': ')
      if studyChoice.lower() == 'f':
        flashcard_style()
        break
      elif studyChoice.lower() == 't':
        test_yourself()
        break
      else:
        print('\nPlease type \'F\' or \'T\'')

    while True:
      studyAgain = input('\nWould you like to study this set again? (Enter Yes or No) ')
      if studyAgain.lower() == 'yes':
        break
      elif studyAgain.lower() == 'no':
        return
      else:
        print('Please enter Yes or No')

def flashcard_style():
  while True:
    orderOrRandom = input('\nWould you like the flashcards to presented in order or randomly? Type in ORDER or RANDOM. ')
    if (orderOrRandom.lower() == 'order' or orderOrRandom.lower() == 'random'):
      break
    else:
      print('Please type in ORDER or RANDOM')
  while True:
    termDef = input('Would you like the term first (type TERM) or definition first (type DEF)? ')
    if (termDef.lower() == 'term' or termDef.lower() == 'def'):
      break
    else:
      print('Please type in TERM or DEF\n')
  
  with open(config.workingFolder + r'/' + workingSet, 'r') as file:
    lineList = file.readlines()
    lenLineList = len(lineList)

    for indece in range(0, lenLineList):
      if orderOrRandom.lower() == 'order':
        tempFlashcard = lineList[indece]
      elif orderOrRandom.lower() == 'random':
        tempFlashcard = random.choice(lineList)
        lineList.remove(tempFlashcard)
      tempFlashcard = tempFlashcard.rstrip('\n').split(chr(0x2588))

      term = tempFlashcard[0]
      definition = tempFlashcard[1]

      if termDef.lower() == 'term':
        outputFormat = {'choice1':'term', 'choice2':'definition', 'var1':term,'var2':definition}
      elif termDef.lower() == 'def':
        outputFormat = {'choice1':'definition', 'choice2':'term', 'var1':definition,'var2':term}
      
      print(('\n{} ' + str(indece+1) + ': {}').format(outputFormat['choice1'], outputFormat['var1']))
      input('\nPress enter when you are ready for the {}: '.format(outputFormat['choice2']))
      print(('\n{} ' + str(indece+1) + ': {}').format(outputFormat['choice2'], outputFormat['var2']))
      if (indece+1) < lenLineList:
        input('\nPress enter when you are ready for the next {}: '.format(outputFormat['choice1']))

def test_yourself():
  while True:
    orderOrRandom = input('\nWould you like the flashcards to presented in order or randomly? Type in ORDER or RANDOM. ')
    if (orderOrRandom.lower() == 'order' or orderOrRandom.lower() == 'random'):
      break
    else:
      print('Please type in ORDER or RANDOM')
  while True:
    termDef = input('Would you like to input the term (type TERM) or the definition (type DEF)? ')
    if (termDef.lower() == 'term' or termDef.lower() == 'def'):
      break
    else:
      print('Please type in TERM or DEF\n')

  with open(config.workingFolder + r'/' + workingSet, 'r') as file:
    lineList = file.readlines()
    lenLineList = len(lineList)

    for indece in range(0, lenLineList):
      if orderOrRandom.lower() == 'order':
        tempFlashcard = lineList[indece]
      elif orderOrRandom.lower() == 'random':
        tempFlashcard = random.choice(lineList)
        lineList.remove(tempFlashcard)
      tempFlashcard = tempFlashcard.rstrip('\n').split(chr(0x2588))

      term = tempFlashcard[0]
      definition = tempFlashcard[1]

      if termDef.lower() == 'term':
        outputFormat = {'choice1':'term', 'choice2':'definition', 'var1':term,'var2':definition}
      elif termDef.lower() == 'def':
        outputFormat = {'choice1':'definition', 'choice2':'term', 'var1':definition,'var2':term}

      guessAgain = 'y'
      while guessAgain == 'y':
        print(('\n{} ' + str(indece+1) + ': {}').format(outputFormat['choice2'], outputFormat['var2']))
        guess = input(('Type in the correct {} to {} ' + str(indece+1) + ': ').format(outputFormat['choice1'], outputFormat['choice2']))
        if guess == outputFormat['var1']:
          input('You got the {} right! Press enter to continue.'.format(outputFormat['choice2']))
          break
        guessAgain = input('Your guess did not match the correct {}. Would you like to try again? '.format(outputFormat['choice1']))
        if guessAgain[0].lower() == 'y':
          guessAgain = 'y'
        else:
          input(('The correct {} to {} ' + str(indece+1) + ' is {}. Press enter to continue').format(outputFormat['choice2'], outputFormat['choice1'], outputFormat['var1']))

def main():
  choiceList = os.listdir(config.workingFolder)
  setChoice = input('\nWhich study set would you like to study from? ')
  for choice in choiceList:
    if choice == (setChoice + '.txt'):
      global workingSet
      workingSet = choice
      study_from_created_set()
      return

  if choice != setChoice:
    print('That study set does not exist. Please try again. ')
    main()

if __name__ == '__main__':
  main()