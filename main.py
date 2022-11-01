import accountlogin as al
import studyoptions as so
import setcreation as sc
import deletion as dn
import config as cg
import editset as es

def menu_input():
  option = -1
  while True:
    option = input('\nEnter 1-8: ')
    try:
      if 1 <= int(option) <= 8:
        break
      else:
        print('Error: Please enter a number 1-8')
    except:
      print('Error: Please enter a number 1-8')
  return option

def main():
  print('\n---------------------------------------------- Welcome to the Flashcards Study App ----------------------------------------------')
  print('This app allows you to create study sets in app and import study sets from both .CSV files and Quizlet sets.')
  print('You also have multiple study options: Flashcards and Self-Testing. Within both options, you can choose if flashcards are ')
  print('presented in their inputted order or a random order. You also have a choice to see the term or definition first.')
  print('To use this app, you will need to have an account. You can also delete your study sets or your account at any time.')
  input('To find your created study sets, locate them in your documents folder. Press enter when you are ready to create/log into an account.')
  
  #Logs in current user - creates account if necessary. 
  al.main()

  run_loop = True
  while run_loop:
    studysetCheck = sc.study_set_check('current')

    print('\nYou have seven possible actions:')
    print('1. Create and save a flashcard set')
    print('2. Import a Quizlet')
    print('3. Import a CSV file located in your desktop')
    print('4. Edit a study set')
    print('5. Study from a created set')
    print('6. Delete a Study Set')
    print('7. Delete your account')
    print('8. End the program')

    #Add option to rename study set
    option = int(menu_input())
    if option == 1:
      studysetCheck = True
      sc.create_and_save_studyset()
    elif option == 2:
      studysetCheck = True
      sc.import_quizlet()
    elif option == 3:
      studysetCheck = True
      sc.import_csv()
    elif option == 4:
      if studysetCheck == False:
        input('\nYou cannot edit from a study set since you do not have any. Please create or import a study set. Press enter to continue')
      else:
        es.main()
    elif option == 5:
      if studysetCheck == False:
        input('\nYou cannot study from a study set since you do not have any. Please create or import a study set. Press enter to continue')
      else:
        sc.study_set_check('current')
        so.main()
    elif option == 6:
      if studysetCheck != False:
        studysetCheck = sc.study_set_check('current')
        while (studysetCheck != False):
          studysetCheck = dn.set_deletion()
          break
      else:
        print('\nYou cannot delete any study sets as you do not have any. Please select a different option.\n')
    elif option == 7:
      if cg.error_control('yes', 'no', '\nAre you sure you want to delete your account? You cannot reverse this. Enter Yes or No. ') == True:
        dn.user_deletion()
        print('\nPROGRAM ENDED\n')
        return
    elif option == 8:
      run_loop = False
  print('\nPROGRAM ENDED\n')

main()