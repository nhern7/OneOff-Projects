import random
import string
import hashlib

alphLower = string.ascii_lowercase
alphUpper = string.ascii_uppercase
alph = string.ascii_letters
PWcollection = open("PWcollection.txt","a")

numGen = []
letGen = []

length = int(input("How long do you want your overall password to be?: "))
numAmount = int(input("Enter the amount of numbers you want your password to include: "))

def letterGenfun():
        for x in range(int(length - len(numGen))):
                letGen.append(random.choice(alph))
                    
def checks(length, numAmount):

        if numAmount > length:
                print("Error! You're asking for more numbers than allowed.")
                length = int(input("How long do you want your password to be?: "))
                numAmount = int(input("Enter the amount of numbers you want your password to include: "))
                checks(length, numAmount)
        elif numAmount == length:
                for x in range(numAmount):    
                        numGen.append(random.randint(0, 9))   
                print("Your password is: ", *numGen, sep='')
                return 
        else:
                for x in range(numAmount):    
                        numGen.append(random.randint(0, 9))         
                letterGenfun()

def passwordFinalization():
        pw = numGen + letGen
        random.shuffle(pw)
        pwEncrypt = hashlib.sha256(str.encode())
        print(pwEncrypt)
        print(*pw, sep='')
        program = input("Enter what program or site this password will be used for: ")
        PWcollection.write("Program: " + program + ' ' + "Password: " + str(pw))

checks(length, numAmount)                
passwordFinalization()
print("Password is added to collection.")


PWcollection.close()

