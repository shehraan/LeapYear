def leap(year):
    if year % 4 != 0:
        print(leap_year)
    elif year % 100 != 0:
        print(leap_year)
    elif year % 400 != 0:
        leap_year = False
    else:
        leap_year = True
    return leap_year

symbols = ["`","~","!","@","$","%","^","&","*","(",")","_","+","=","/","{","}","|",":",",","<",">","?","'",'"',"[","]"]
numbers = ["1","2","3","4","4","5","6","7","8","9","0"]

#Symbolchecker
def symbol(word):
    for letters in word:
        if (letters in symbols)==True:
            return True
    return False

#Numberchecker
def number(word):
    for letters in word:
        if (letters in numbers)==True:
            return True
    return False
while True:
    year = input("Please enter the year: ")
    while symbol(year)==True or any(i.isalpha() for i in year)==True or number(year)==True:
        if symbol(year)==True:
            print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
            year = input("Please enter the year: ")
        if any(i.isalpha() for i in year)==True:
            print("Error, you entered a letter which is an invalid input. Please only enter a positive number.")
            year = input("Please enter the year: ")
        if number(year)==True:
            if float(year)<0:
                print("Error, you have entered a negative year which is impossible. Please enter a positive number.")
                year = input("Please enter the year: ")
            else:
                break
    print("\nleap year = "+str(leap(400))+"\n")
    
    redo = (input("If you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
    while redo!="y" and redo!="n":
        print("Error, please enter one of the given options")
        redo = (input("If you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
    if redo=="n":
        break
    else:
        print("\nRestarting program\n")