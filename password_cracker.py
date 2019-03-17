rainbow_table = {}
stole_data = {}
import hashlib
import os.path

def hasher(password):
    b = bytes(password, 'utf-8')
    m = hashlib.sha256(b)
    m = m.hexdigest()
    return m
    
def create_rainbow_table():
    file = open ("user_data.txt", 'r')
    for line in file:
        line = line.strip("\n")
        bad_passwords = hasher(line)
        rainbow_table[bad_passwords] = line
    file.close()

def stolen_data():
    file = open("user_data.txt", 'r')
    for line in file:
        words = line.split("'")
        print(words)
        username = words[0]
        bad_passwords = words[1]
        stole_data[bad_passwords] = username
    file.close()

def cracked_passwords():
    file = open ("cracked_passwords.txt", 'a+')
    for bad_password in rainbow_table:
        if stole_data.get(bad_password):
            username = stole_data[bad_password]
            password = rainbow_table[bad_password]
            print("hi")
            file.write(username + " " + password + "\n")
    file.close()



create_rainbow_table()
print(rainbow_table)
stolen_data()
cracked_passwords()

        

            


            

        
