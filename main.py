#Welcome page
def welcom():
    print()
    print('Welcome to XYZ HealthTip')
    print()
    name = input('ENTER USERNAME: ')
    pw = input('ENTER PASSWORD: ')
    detail()
    back()
#first command detail()
def detail():
    print()
    print('Hello', (name))
    print('How do you like to use our service today?')
    print()
    print('1) Genotype Compatibility check')
    print('2) Rh+/Rh- Counselling')
    print('3) Others')
    print('4) Book a one on one session')
    print()
    R = input('Reply: ')
    if R == '1':
        print()
        comp()
    return
#Second command comp()
def comp ():
    sp1 = input('Enter your genotype: ')
    sp2 = input('Enter partner genotype: ')
    if sp1 == 'AA' and sp2 == 'AA':
        print()
        print('Status: Compatible')
        print('Comment: Okay')
    elif sp1 == 'AS' and sp2 == 'AA' or sp1 == 'AA' and sp2 == 'AS':
        print()
        print('Status: Compatible')
        print('Comment: Okay')
    elif sp1 == 'AA' and sp2 == 'SS' or sp1 == 'SS' and sp2 == 'AA':
        print()
        print('Status: Compatible')
        print('Comment: Seek counselling')
    elif sp1 == 'AS' and sp2 == 'AS':
        print()
        print('Status: Incompatible')
        print('Comment: Seek counselling')
    elif sp1 == 'SS' and sp2 == 'SS':
        print()
        print('Status: Incompatible')
        print('Comment: Seek counselling')
    elif sp1 == 'AS' and sp2 == 'SS' or sp1 == 'SS' and sp2 == 'AS':
        print()
        print('Status: Incompatible')
        print('Comment: Seek counselling')
    else:
        print ('Wrong input, make sure genotypes are correctNA')
    return

#Last command back()
def back():
    print()
    b = input('Press 0 to go back'
              'Press 00 to exit :')
    if b == '0':
        print('---------------------------------------------------------')
        print()
        #Return to  first command
        detail()
        back()
    elif b == '00':
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        welcom()
    else:
        print('Bye')

    return
#Welcom page
print()
print ('Welcome to XYZ HealthTip')
print()
name = input('ENTER USERNAME: ')
pw = input ('ENTER PASSWORD: ')
detail()
back()

