import os
import config
import setcreation as sc

def print_pairs(workingSet):
    with open(config.workingFolder + r'/' + workingSet, 'r') as workingFile:
        lines = workingFile.readlines()

    flashcards = {}
    print('\nThe terms and definitions in studyset {} are: \n'.format(workingSet.rstrip('.txt')))
    counter = 1
    for line in lines:
      tempList = line.rstrip('\n').split(chr(0x2588))
      flashcards[tempList[0]] = tempList[1]
      print('Term {}: {}\nDefinition {}: {}\n'.format(counter, tempList[0], counter, tempList[1]))
      counter +=1
    return counter, lines, flashcards

#Need to make sure edited values are not empty terms or defs, terms named no, or repeats
def edit_current_card(file, lines, termDefLength, flashcards):
    flashcards = {}
    for line in lines:
      tempList =  line.rstrip('\n').split(chr(0x2588))
      flashcards[tempList[0]] = tempList[1]

    while True:
        editTerm = input('\nWhich term would you like to edit? Enter a number between 1 and {}: '.format(termDefLength-1))
        if int(editTerm) in range(0,termDefLength):
            break
        else:
            print('{} is not in range. Please Pick a number in range'.format(editTerm))

    term = False
    definition = False
    count = 0
    for line in lines:
      count+=1
      if count == int(editTerm):
        editLine = line.rstrip('\n').split(chr(0x2588))
        print('\nThe current term is: {}'.format(editLine[0]))
        print('The current definition is: {}'.format(editLine[1]))
        while term == False or definition == False:
          term, definition = sc.set_creation_output(input("\nEnter the new term: "), input("Enter the new definition: "), flashcards,
            'You cannot enter a blank term or definition. Please try again.',
            'You cannot have a term named \'No\'. Please enter a differently named term',
            'This term is a repeat. Please enter a different term.')
        
        flashcards[term] = flashcards.pop(editLine[0])
        editLine[0] = term
        flashcards[editLine[0]] = definition
        sc.write_file(file, flashcards, 'w')

        print('\nThe new term is: {}'.format(editLine[0]))
        print('The new definition is: {}\n'.format(flashcards[editLine[0]]))

        editMore = config.error_control('yes', 'no', '\nWould you like to edit another flashcard? (Enter Yes or No) ')
        if editMore == True:
          edit_current_card(file, lines, termDefLength, flashcards)

def add_flashcards(file, flashcards):
    while True:
      term, definition = sc.set_creation_output(input("\nEnter term: "), input("Enter definition: "), flashcards,
        'You cannot enter a blank term or definition. Please try again.',
        'You cannot have a term named \'No\'. Please enter a differently named term',
        'This term is a repeat. Please enter a different term.')
      if term != False:
        flashcards[term] = definition
      if config.error_control('yes', 'no', '\nWould you like to add another flashcard? (Enter Yes or No) ') != True:
        break

    sc.write_file(file, flashcards, 'w')
    print('The term/def pair has been successfully added\n')

def delete_termdef(file):
  flashcards = {}
  with open(file, 'r') as textFile:
    termDef = textFile.readlines()
    if len(termDef) <= 5:
      input('\nYou cannot have less than 5 term/def pairs. Press enter to continue')
      return

  pairNum = input('\nWhich number term/def pair do you want to delete? If you would not like to delete a pair, enter \'No\' ')
  if pairNum.lower() == 'no':
    return
  
  counter = 0
  for pair in termDef:
    counter +=1
    if counter != int(pairNum):
      tempList = pair.rstrip('\n').split(chr(0x2588))
      flashcards[tempList[0]] = tempList[1]

  sc.write_file(file, flashcards, 'w')
  print('\nYou have successfully deleted term/def pair {}.\n'.format(pairNum))

def main():
  #Prints current study sets
  sc.study_set_check('current')

  #User chooses which set to study from
  setFound = False
  while setFound == False:
    editingSet = input('\nEnter the number of the set you would like to edit. If you only have 1 set, enter (1). If you would not like to study from a created set, enter \'No\' ')
    if editingSet.lower() == 'no':
      return

    choiceList = os.listdir(config.workingFolder)
    choiceList.sort()

    try:
      os.remove(config.workingFolder + r'/.DS_Store')
    except:
      pass

    try:
      editingSet = int(editingSet)-1
      for indece in range(0, len(choiceList)):
        if (editingSet) == indece:
          global workingSet
          workingSet = choiceList[editingSet]
          setFound = True
          break
      else:
        print('Please enter a number between 1 and {} '.format(len(choiceList)))
    except:
      print('Please enter a number between 1 and {}'.format(len(choiceList)))

  #edits study set
  setPath = os.path.join(config.workingFolder, workingSet)
  while True:
    counter, lines, flashcards = print_pairs(workingSet)
    userInput = input('If you would like to edit an existing term/def pair, type \'E\'. If you would like to add more items to your study set, type \'A\'. If you would like to delete a term and definition, type \'D\'. If you would not like to edit your set, enter \'No\' ').lower()
    if userInput == 'e':
      edit_current_card(setPath, lines, counter, flashcards)
    elif userInput == 'a':
      add_flashcards(setPath, flashcards)
    elif userInput == 'd':
      delete_termdef(setPath)
    elif userInput.lower() == 'no':
      break
    else:
      print('Please answer {}, {}, or {}'.format('E', 'A', 'D'))
  
  if __name__ == "__main__":
    main()
