alphabet = "abcdefghijklmnopqrstuvwxyz"
newAlphabet = ""

secretMessage = (input("Enter a messsage you would like to encrypt:"))

for key in range(0, 11):
    newAlphabet = alphabet[key:] + alphabet[:key]
    attempt = ""
    for i in range (0 , len(secretMessage)):
        index = alphabet.find(secretMessage[i])
        attempt += newAlphabet[index]
    print ("Key " + str(key) + " attempt")
    print (attempt)

    
""" 
key = int(input("Enter the amount to shift by:"))
if key < 0:
   key += 26

newAlphabet = alphabet[x:] + alphabet[:x]

newMessage = ""

for letter in mesasage:
    index = alphabet.find(letter)

    newMessage += newAlphabet(index)
    
print (newMessage)

message = (input("Enter a messsage:"))
"""
