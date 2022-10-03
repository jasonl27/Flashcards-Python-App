import os
import config

def study_set_check(outputControl):
  allFiles = os.listdir(config.workingFolder) 
  fileList = []
  counter = 0
  for file in allFiles:
    if not file.endswith('.DS_Store'):
      counter += 1
      fileList.append(file)
    elif file == '.DS_Store':
        os.remove(config.workingFolder + r'/' + file)

  if (allFiles == [] or allFiles == ['.DS_Store']):
    print('You do not have any flashcard sets.\n')
    return False
  elif counter == 1:
    print('Your only set is: {}'.format(fileList[0].rsplit('.', 1)[0]))
  elif len(fileList) > 1:
    print('\nThese are your {} study sets:'.format(outputControl))
    for file in fileList:
        print('You have a set called: {}'.format(file.rsplit('.', 1)[0]))

def create_and_save_studyset():
  fileName = input('What would you like to name your flashcard set? ')
  workingDirectory = os.listdir(config.workingFolder)

  for file in workingDirectory:
    if (file == fileName + '.txt' or file == fileName):
      print('A file with this name already exists. Please try using a different file name.')
      create_and_save_studyset()

  filePath = os.path.join(config.workingFolder + r'/' + fileName + '.txt')
  flashcards = {}

  while True:
    term = input("\nEnter term: ")
    definition = input("Enter definition: ")

    #Stops user from inputting unwanted terms or definitions
    if (term == '' or definition == ''):
      print('You cannot enter a blank term or definition. Please try again.')
    elif term.lower() == 'no':
      print('You cannot have a term named \'No\'. Please enter a different termname')
    elif term in flashcards:
      print('This term is a repeat. Please enter a different term.')

    flashcards[term] = definition

    #Checks to see if user wants to add another flashcard. Control for unwanted inputs
    while True:
        str = input('\nWould you like to add another flashcard? (Enter Yes or No) ')
        if str.lower() == 'yes':
          break
        elif str.lower() == 'no':
          break
        else:
          print('Please enter Yes or No. ')
    if str.lower() == 'no':
        break

  with open(filePath, 'a') as termsAndDef: 
    for key, value in flashcards.items(): 
      termsAndDef.write('{}{}{}\n'.format(key, chr(0x2588), value))

def set_deletion():
  while True:
    allFiles = os.listdir(config.workingFolder)

    deleteSet = input('\nWhich set would you like to delete? If you would not like to delete a set, type \'No\': ')
    if deleteSet.lower() == 'no':
      break
    deleteSet += '.txt'

    #Deletes set and confirms it
    found = False
    for file in allFiles:
      if file == deleteSet:
        os.remove(config.workingFolder + r'/' + file)
        allFiles.remove(file)
        print('\n{} was successfully deleted.\n'.format(file.rsplit('.', 1)[0]))
        found = True
        break

    if not found:
        print('File {} does not exist. Please try deleting an existing file.'.format(deleteSet.rsplit('.', 1)[0]))
        set_deletion()

    #Prints remaining study sets
    study_set_check('remaining')
    if allFiles == []:
        break

    #Loops again if user wants to delete another file. Escapes function if user does not
    deleteFile = True
    while deleteFile == True:
        continueDelete = input('\nWould you like to delete another file? Enter Yes or No. ')
        if continueDelete.lower() == 'yes':
            break
        elif continueDelete.lower() == 'no':
            return
        else:
            print('Please enter Yes or No.')