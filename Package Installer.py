import os

def trynow():
    try:
        os.system('pip install tk')
        print('\n\nAll Packages are succesfully installed')
         input('Press Enter to Exit')

    except:
        print('\nSomthing Went Wrong\n')
        input('Press Enter to exit [ENTER]')
        
try:
    os.system('pip install tk')
    print('\n\nAll Packages are succesfully installed')
    input('Press Enter to Exit')

except:
   print('\nSomthing Went Wrong\n')
   input('Press Enter to try again')
   os.system('cls')
   trynow()
