import os
import config
import getpass

def check_account():
    while True:
        username = input('What is your username? ')
        #Checks username.txt for user's inputted username
        with open('username.txt', 'r') as searchUsername:
            textFileSearch = searchUsername.readlines()
            for row in textFileSearch:
                findUserName = row.find(username)
                if findUserName == 0:
                    print('\nWelcome back, {}.'.format(username))
                    global workingFolder
                    workingFolder = r'/Users/' + getpass.getuser() + r'/Documents/Flashcards Program/Users/' + username
                    config.workingFolder = workingFolder
                    #return instead of break - return ends function rather than just breaking loop
                    return

        #this code will only run if the user inputted username was not found
        print('\n{} is not a registered username.\n'.format(username))
        if config.error_control('yes', 'no', 'Are you sure you have an account? If you have an account, enter \'Yes\'. If you do not, enter \'No\' ') == False:
            create_account()
            break


def create_account():
  while True:
    username = input('\nCreate a username for your account. If you already have an account, type \'have account\': ')
    if username.lower() == 'have account':
        check_account()
        return

    try:
        if username == '\'\'' or username == '\"\"' or username == '\n':
            raise Exception('Cannot use \"{}\" as a username'.format(username))

        newPath = os.path.join(r'/Users/' + getpass.getuser() + r'/Documents/Flashcards Program/Users/' + username)
        os.makedirs(newPath)

        with open('username.txt', 'a') as usernameHolder:
            usernameHolder.write(username + '\n')
        print('\nYour account has successfully been created. You are currently logged in as: {}\n'.format(username))
        config.workingFolder = newPath
        break
    except Exception:
        print('\nCannot use \"{}\" as a username. Please try a different one. '.format(username))
    except:
        print('This user has already been created. Please try another username.')

def main():
    if config.error_control('yes','no', '\nDo you have an account? (Enter Yes or No) ') == True:
        check_account()
        return
    else:
        create_account()
        return
  #User account is confirmed by this point. 'Welcome back user' message pops up

if __name__ == "__main__":
    main()