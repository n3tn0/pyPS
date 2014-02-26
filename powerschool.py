__author__ = 'tim'

import powerapi
from getpass import getpass
import sys

ps = powerapi.core('https://stafford.powerschool.com')

#Print basic header information
print('pyPowerSchool')
print('A POWERSCHOOL COMMAND LINE APP WRITTEN IN PYTHON')
print('BY: TIMOTHY NOTO (n3tn0)')
print('VERSION: ALPHA')
print('\n\n')

#Get the user's PowerSchool information and authenticate it
username = raw_input('PowerSchool Username: ')
password = getpass('Password: ')
try:
    user = ps.auth(username, password)
except Exception as err:
    print "Sorry! User or password incorrect.", err
    sys.exit()
print('\nWelcome to ' + user.getUserName() + '!')

#Print the main menu and prompt the user for their selection
print('Main Menu:\n')
print('[1] Scores')
print('[2] GPA')
print('[3] Averages & Analysis')
print('[4] Attendance')
print('[5] Teachers\n')
choice = int(raw_input('Enter menu number: '))

courses = user.getCourses()
#Determine the user's menu choice
if choice == 1:
    print('[1] All Classes')
    x = 2
    for i in range(1, len(courses)):
        print('[%i] %s' % (x, courses[i].getName()))
        x += 1
    choice = int(raw_input('Enter menu number: '))
    if choice == 1:
        pass
    else:
        print(courses[choice+1].getScores())
elif choice == 2:
    pass
elif choice == 3:
    pass
elif choice == 4:
    pass
elif choice == 5:
    pass
else:
    print('Fail!')
