import random
import string

alphLower = string.ascii_lowercase
alphUpper = string.ascii_uppercase
alph = string.ascii_letters
PWcollection = open("PWcollection.txt","a")

numGen = []
letGen = []

length = int(input("How long do you want your overall password to be?: "))
numAmount = int(input("Enter the amount of numbers you want your password to include: "))

def letterGenfun():
        capitalsIncluded = str(input("Do you want to enable capital letters in the generator? Y or N: "))
        if capitalsIncluded == 'Y':
                for x in range(int(length - len(numGen))):
                        letGen.append(random.choice(alph))
        elif capitalsIncluded == 'N':
                for x in range(int(length - len(numGen))):
                        letGen.append(random.choice(alphLower))
        else: 
                print("Error! You entered an invalid character.")
                letterGenfun()
    
                
def checks(length, numAmount):

        if numAmount > length:
                print("Error! You're asking for more numbers than allowed.")
                length = int(input("How long do you want your password to be?: "))
                numAmount = int(input("Enter the amount of numbers you want your password to include: "))
                checks(length, numAmount)
        elif numAmount == length:
                numRange = int(input("Enter the highest number in a range of numbers to include: "))
                for x in range(numAmount):    
                        numGen.append(random.randint(0, numRange))   
                print("Your password is: ", *numGen, sep='')
                return #change to a continuation
        else:
                numRange = int(input("Enter the highest number in a range of numbers to include: "))
                for x in range(numAmount):    
                        numGen.append(random.randint(0, numRange))         
                letterGenfun()
                

checks(length, numAmount)

pw = numGen + letGen
random.shuffle(pw)
print(*pw, sep='')
program = input("Enter what program or site this password will be used for: ")
PWcollection.write("Program: " + program + ' ' + "Password: " + str(pw))

print("Password is added to collection.")

PWcollection.close()
#continuation
