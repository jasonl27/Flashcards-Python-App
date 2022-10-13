import os
import config
import getpass
from setcreation import study_set_check

def set_deletion():
  while True:
    deleteSet = input('\nWhich set would you like to delete? If you would not like to delete a set, type \'No\': ')
    if deleteSet.lower() == 'no':
      break
    deleteSet += '.txt'

    #Deletes set and confirms it
    allFiles = os.listdir(config.workingFolder)
    for file in allFiles:
        line = config.workingFolder + r'/' + file
        if file == deleteSet:
            os.remove(line)
            allFiles.remove(file)
            print('\n{} was successfully deleted.'.format(file.rsplit('.', 1)[0]))
            break
    else:
        print('File {} does not exist. Please try deleting an existing file.'.format(deleteSet.rsplit('.', 1)[0]))
        set_deletion()

    if study_set_check('remaining') == False:
        return False
    if config.error_control('yes', 'no', '\nWould you like to delete another file? Enter Yes or No. ') != True:
        break

def user_deletion():
  #Removes all files in directory, then user folder
  for file in os.listdir(config.workingFolder):
    os.remove(config.workingFolder + r'/' + file)
  os.rmdir(config.workingFolder)
  
  #Rewrites username.txt file without user who is being deleted
  with open('username.txt', 'r') as textFile:
    usernameList = textFile.readlines()
  with open('username.txt', 'w') as usernameFile:
    for username in usernameList:
      if (config.workingFolder + '\n') == ((r'/Users/' + getpass.getuser() + r'/Documents/Flashcards Program/Users/') + username):
        pass
      else:
        usernameFile.write(username)

  print('\nACCOUNT DELETED')