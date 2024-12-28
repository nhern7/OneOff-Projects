user_data = {}
salts = []
import hashlib
import os.path


def hasher(password):
    b = bytes(password, 'utf-8')
    m = hashlib.sha256(b)
    m = m.hexdigest()
    return m

def get_salt(password):
    last_letter = password[-1].lower()

    indexA = ord('a')
    indexL = ord(last_letter)
    index = indexL - indexA
    salt = salts[index]

    return salt

    
def read_salts():
    file = open("salt_list.txt", "r")
    for line in file:
        salts.append(line.strip("\n"))
    file.close()
    

def read_file():
    if not os.path.isfile("user_data.txt"):
        return
    file = open("user_data.txt", "r")            

    for line in file:
        info = line.split("'")
        username = info[0]
        password = info[1]
        birthday = info[2]
        inbox = info[3].strip("\n")
        inbox = inbox.split("^")
        inbox.pop()
        print (inbox)  
        user_data[username] = [password, birthday, inbox]

    file.close()
        
def write_users():
    file = open("user_data.txt", 'w')
    for user in user_data:
        
        info = user + "'" + user_data[user][0] + "'" + user_data[user][1] + "'"
        file.write(info)
        inbox = user_data[user][2]
        for email in inbox:
            file.write(email + "^")
        file.write("\n")
    file.close()
    
def view():
    inbox = user_data[username][2]
    
    print (user_data.keys())
    for email in inbox:
        print (email)
    
def choice():
    choice = (input("Enter V to view info or S to send:"))
    if choice == "V":
        view()
    if choice == "S":
        send()

def send():
    prompt = (input("Who would you lke to send mail to:"))
    if not user_data.get(prompt):
        print("Error, enter valid name.")
        return
    
    msg_sending = (input("Please compose the message you would like to send:"))
    prompt_inbox  = user_data[prompt][2]

    prompt_inbox.append(msg_sending)
                
def login():
    print ("Logging In..")


    username = (input("Enter your username:"))
                    
    if not user_data.get(username):
        print("Error, invalid name.")
        return 

    password = (input("Confirm your password:"))
    salt = get_salt(password)
    hashed_password = hasher(password)
    salted_password = hasher(password + salt)
    
    correct_password = user_data[username][0]

    
    tries = 0
    x = 1

    while x == 1:
        if correct_password == hashed_password:
            print ("Welcome Back.")
            choice()

        else:
            if tries <= 5:
                print ("Invalid, try again.")
                tries += 1
                password = (input("Confirm your password:"))
                salt = get_salt(password)
                hashed_password = hasher(password)
                salted_password = hasher(password + salt)

            elif tries > 5:
                print ('Attemptd tries are up. Locked out.')
                exit()
    

def create_account():
    username = (input("Enter a username:"))
    password = (input("Enter a password:"))
    salt = get_salt(password)
    hashed_password = hasher(password)
    salted_password = hasher(password + salt)
    
    birthday = (input("Enter your birthday:")) 
    inbox = ["Welcome to the email inbox"]
    user_data[username] = [hashed_password, birthday, inbox]

read_file()
read_salts()
write_users()
                 
message = (input("Enter C to create an account, or L to login, or Q to quit:"))

while message != "Q":
    if message == "C":
        print ("Creating Account..")
        create_account()
        message = (input("Enter C to create an account, or L to login, or Q to quit:"))
        
    elif message == "L":
        login()

    else:
        print ("Pick a valid option:")
        message = (input("Enter C to create an account, or L to login, or Q to quit"))


