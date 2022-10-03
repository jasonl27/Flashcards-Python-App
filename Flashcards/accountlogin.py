import os
import config

def check_account():
    username = input('What is your username? ')
    #Checks username.txt for user's inputted username
    with open('username.txt', 'r') as searchUsername:
        textFileSearch = searchUsername.readlines()
        for row in textFileSearch:
            findUserName = row.find(username)
            if findUserName == 0:
                print('\nWelcome back, {}.' .format(username))
                global workingFolder
                workingFolder = r'~/' + username
                config.workingFolder = workingFolder
                #return instead of break - return ends function rather than just breaking loop
                return

    #this code will only run if the user inputted username was not found
    print('\n' + username + ' is not a registered username.\n')

    loopBreak = input('Are you sure you have an account? If you do not have an account, type \'create account.\' ')
    if loopBreak.lower() == 'create account':
      create_account()
    else:
      check_account()

def create_account():
  username = input('\nCreate a username for your account. If you already have an account, type \'have account\': ')
  
  if username.lower() == 'have account':
    check_account()
    return

  #try: - tries to create a (folder) with the user's name within FLASHCARDS program - will store study sets (.txt files)
  try:
    if username == '\'\'' or username == '\"\"':
        raise Exception('Cannot use {} as a username'.format(username))

    newPath = os.path.join(r'~/' + username)
    os.makedirs(newPath)

    with open('username.txt', 'a') as usernameHolder:
      usernameHolder.write(username + '\n')
    
    print('\nYour account has successfully been created. You are currently logged in as: ' + username + '\n')
    config.workingFolder = newPath

  #Try: code will fail if the user-inputted code already has a folder created w/same name
  #Except: catches error and asks user to try a different username
  except Exception:
    print('\nCannot use {} as a username. Please try a different one. '.format(username))
    create_account()
  except:
    print('This user has already been created. Please try another username.')
    create_account()

def main():
  userAccount =input('\nDo you have an account? (Enter Yes or No) ')
  if userAccount.lower() == 'yes':
    check_account()
  elif userAccount.lower() == 'no':
    create_account()
  else:
    print('Please enter Yes or No to continue.')
    main()
  #User account is confirmed by this point. 'Welcome back user' message pops up

if __name__ == "__main__":
    main()