import os
import config
import getpass
from setcreation import study_set_check

#Need to select deleting set by number
def set_deletion():
  setFound = False
  while setFound == False:
    deleteSet = input('\nEnter the number of the set you would like to delete. If you only have 1 set, enter (1). If you would not like to study from a created set, enter \'No\' ')
    if deleteSet.lower() == 'no':
      return

    choiceList = os.listdir(config.workingFolder)
    choiceList.sort()

    try:
      os.remove(config.workingFolder + r'/.DS_Store')
    except:
      pass

    try:
      for file in choiceList:
        line = config.workingFolder + r'/' + file
        if file == choiceList[int(deleteSet)]:
            os.remove(line)
            choiceList.remove(file)
            print('\n{} was successfully deleted'.format(file.rsplit('.', 1)[0]))
            break
      else:
        print('Please enter a number between 1 and {} '.format(len(choiceList)))
    except:
      print('Please enter a number between 1 and {}'.format(len(choiceList)))
    if config.error_control('yes', 'no', '\nWould you like to delete another file? Enter Yes or No. ') != True:
      break
    else:
      study_set_check('current')

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