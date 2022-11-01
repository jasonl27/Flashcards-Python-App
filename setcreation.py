import os
import csv
import getpass
import config

#Checks for study sets; prints list of created study sets
def study_set_check(outputControl):
  fileList = []
  counter = 0
  for file in os.listdir(config.workingFolder):
    if not file.endswith('.DS_Store'):
      counter += 1
      fileList.append(file)
  fileList.sort()

  if counter == 1:
    print('Your only Set is: {}'.format(fileList[0].rsplit('.', 1)[0]))
  elif counter > 1:
    print('\nThese are your {} study sets:'.format(outputControl))
    counter = 1
    for file in fileList:
      counter += 1
      print('Set ({}) is called: {}'.format(int(counter)-1, file.rsplit('.', 1)[0]))
  else:
    print('You do not have any study sets.\n')
    return False

#Gets name of flashcard set; allows user to exit set creation; checks to see if user-chosen file name already exists
def set_creation_check():
  while True:
    userInput = input('What would you like to name your study set? If you would not like to create a set, type \'No\' ')
    if userInput.lower() == 'no':
      return False
    else:
      for file in os.listdir(config.workingFolder):
        if (file == userInput + '.txt' or file == userInput):
          print('A file with this name already exists. Please try using a different file name.\n')
          break
      else:
        return userInput

#Formats output
def set_creation_output(term, definition, flashcards, output1, output2, output3):
  if (term == '' or definition == ''):
    print(output1)
    return False, False
  elif term.lower() == 'no':
    print(output2)
    return False, False
  elif term in flashcards:
    print(output3)
    return False, False
  else:
    return term, definition

#Writes flashcard .txt file
def write_file(filepath, flashcards, accesstype):
  with open(filepath, accesstype) as termsAndDef: 
    for key, value in flashcards.items(): 
      termsAndDef.write('{}{}{}\n'.format(key, chr(0x2588), value))

#Creating study set through app
def create_and_save_studyset():
  userInput = set_creation_check()
  if userInput == False:
    return

  print('\nYou need at least 5 Term/Definition pairs to create a functional study set.')

  flashcards = {}
  while True:
    while len(flashcards) < 5:
      term, definition = set_creation_output(input("\nEnter term: "), input("Enter definition: "), flashcards,
        'You cannot enter a blank term or definition. Please try again.',
        'You cannot have a term named \'No\'. Please enter a differently named term',
        'This term is a repeat. Please enter a different term.')
      if term != False:
        flashcards[term] = definition
    if config.error_control('yes', 'no', '\nWould you like to add another flashcard? (Enter Yes or No) ') != True:
      break
    
  write_file(os.path.join(config.workingFolder + r'/' + userInput + r'.txt'), flashcards, 'a')

#Importing Quizlet
def import_quizlet():
  print('\nTo import from Quizlet, follow these steps:\n')
  print('1. Go to the set which you want to export on Quizlet, and make sure you do not have any terms/definitions which span multiple lines.')
  print('2. Then, scroll down to find the three dots. (Located between the large flashcard and individual terms, near the top)')
  print('3. Click on the three dots, then click export')
  print('4. Select \'Other\' for the \'Between term and definition\' section, and put two dashes (--). Then, select \'New Line\' for the \'Between rows\' section.')
  print('5. Optionally check of \'Alphabetize section\'')
  print('6. Press copy text. Once you have copied your text, name your set and paste it')
  print('7. When you have imported your set, press enter twice.\n')
  
  userInput = set_creation_check()
  if userInput == False:
    return
    
  #Captures pasted study sets
  setList = input('Input here: ')
  text = []
  while True:
    setList = input('')
    if setList == '':
      break
    text.append(setList)

  counter = 0
  flashcards = {}
  for list in text:
    counter += 1
    tempList = list.split('--')

    term, definition = set_creation_output(tempList[0], tempList[1], flashcards,
      '\nThere is an empty term/def in row {}. Empty spaces are not allowed. This row has not been added to your study set.'.format(counter),
      '\nThere is a term named \'No\' in row {}. Terms cannot be named \'No\'. This row has not been added to your study set.'.format(counter),
      '\nThe term in row {} is a repeat. Terms cannot be repeated. This row has not been added to your study set.'.format(counter))

    if term!= False:
      flashcards[term] = definition
        
  write_file(os.path.join(config.workingFolder + r'/' + userInput + r'.txt'), flashcards, 'a')

#importing CSV
def import_csv():
  userInput = set_creation_check()
  if userInput == False:
    return

  while True:
    print('\nTo import a .CSV file:')
    print('1. Make sure your file has two columns: the leftwards one containing terms and the rightwards one containing definitions.')
    print('2. Make sure you have at least 5 valid Term/Definition pairs to function as a study set.')
    print('3. Remember to include the full name of the file, including the .CSV extension.\n')

    fileName = input('What is the full name of the .csv file you are importing? ')
    desktopFiles = os.listdir(r'/Users/' + getpass.getuser() + r'/Desktop/')
    for file in desktopFiles:
      if fileName == file:
        break
    if fileName == file:
      break
    print('CSV file {} does not exist. Please try another file name.\n'.format(fileName))

  #this only checks desktop - when building GUI, add 'dropbox' option
  with open(r'/Users/' + getpass.getuser() + r'/Desktop/' + fileName, 'r') as file:
    reader = csv.reader(file)

    flashcards = {}
    counter = -1
    for row in reader:
      counter += 1
      term, definition = set_creation_output(row[0], row[1], flashcards,
        '\nThere is an empty term/def in row {}. Empty spaces are not allowed. This row has not been added to your study set.'.format(counter),
        '\nThere is a term named \'No\' in row {}. Terms cannot be named \'No\'. This row has not been added to your study set.'.format(counter),
        '\nThe term in row {} is a repeat. Terms cannot be repeated. This row has not been added to your study set.'.format(counter))
            
      if term != False:
        flashcards[term] = definition

  if len(flashcards) < 5:
    print('\nYou cannot have a flashcards set with less than 5 terms. Please try a different .CSV file.')
  else:
    write_file(os.path.join(config.workingFolder + r'/' + userInput + r'.txt'), flashcards, 'a')
    print('\nSET CREATED\n')