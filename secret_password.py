right_answer = "hello"
input_answer = str(input("enter the secret password:"))
def password_check(input_answer):
    if input_answer == right_answer: 
        print ("correct")
    else:
        print ("wrong entry, try again")
        
password_check(input_answer)


    
