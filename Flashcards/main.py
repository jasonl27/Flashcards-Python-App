import os
import accountlogin
import studyoptions
import filemanipulation
import config

def user_deletion():
  allFiles = os.listdir(config.workingFolder)
  for file in allFiles:
    os.remove(config.workingFolder + r'/' + file)

  os.rmdir(config.workingFolder)

  print('\nACCOUNT DELETED')

def main():
  #Logs in current user - creates account if necessary. 
  accountlogin.main()

  actionsLeft = True
  while actionsLeft == True:
    #Returns list of user-created study sets
    studysetCheck = filemanipulation.study_set_check('current')

    #Gives user option to study from a set only if there is a list of (1 or more) study sets
    while studysetCheck != False:
      studyFromSet = input('\nWould you like to study from a created set? (Enter Yes or No) ')
      if studyFromSet.lower() == 'yes':
        filemanipulation.study_set_check('current')
        studyoptions.main()
        break
      elif studyFromSet.lower() == 'no':
        break
      else:
        print('Please answer Yes or No. ')

    #gives user option to create a new flashcard set. While loop is used for input control
    while True:
      newSet = input('Would you like to create a new flashcard set? (Enter Yes or No) ')
      if newSet.lower() == 'yes':
        studysetCheck = True
        print('\n')
        filemanipulation.create_and_save_studyset()
        print('\n')
        break
      elif newSet.lower() == 'no':
        break
      else:
        print('Please enter Yes or No.\n')

    #only lets you delete sets if you have more than one set - stops giving user option to delete a set they just made
    while (studysetCheck != False):
      studysetCheck = filemanipulation.study_set_check('current')

      setDeleteInput = input('\nWould you like to delete a study set? Enter Yes or No. ')
      if setDeleteInput.lower() == 'yes':
        filemanipulation.set_deletion()
        break
      elif setDeleteInput.lower() == 'no':
        break
      else:
        print('Please answer Yes or No\n')
    
    while True:
      accountDelete = input('Would you like to delete your account? ')
      if accountDelete.lower() == 'yes':
        accountDelete = input('Are you sure you want to delete your account? You cannot reverse this. Enter Yes or No. ')
        if accountDelete.lower() == 'yes':
          actionsLeft = False
          user_deletion()
          print('\nPROGRAM ENDED\n')
        return
      elif accountDelete.lower() == 'no':
        break
      else:
        print('Please enter Yes or No.')
  
    while True:
      userOption = input('Would you like to do anything else? (Enter Yes or No) ')
      if userOption.lower() == 'yes':
        break
      elif userOption.lower() == 'no':
        print('\nPROGRAM ENDED\n')
        return
      else:
        print('Please answer Yes or No\n')

main()