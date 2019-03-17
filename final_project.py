import random
import math

def bitwise(checksum,flag):
    answer = ""

    for i in range(0,len(checksum)):
        if checksum[i] == '0' and flag[i] == '0':
            answer += '0'

        else:
            answer += '1'

    return answer

def getchecksum():
    SYN_rand = random.randint (0,40)
    ACK_rand = random.randint (0,40)
    checksum = "00000000"
    if SYN_rand < 33:
        SYN_flag = "11110000"

    else:
        SYN_flag = "00000000"

    checksum = bitwise(checksum, SYN_flag)

    if ACK_rand < 33:
        ACK_flag = "00001111"

    else:
        ACK_flag = "00000000"

    checksum = bitwise(checksum, ACK_flag)

    return checksum


def binaryThing(num):
    global binary_num
    binary_num = [0] * 32
    while num > 0:
        L = int(math.log(num, 2))
        num = num - (2 ** L)
        binary_num[32 - L - 1] = 1
    return binary_num
        

def send2Server():
    global target_server
    print ("Byte[s] sending..")
    target_server = host[:bs]
    print (target_server)
    return target_server

def reSend():
    rand_num = random.randint (0,40)
    if rand_num > 33:
        print ('Error. Package could not be received by server.')
        exit()
    else:
        print ('Resending packet.')
        target_server = send2Server()

user_input = (input("Do you want to enter an int(i) or a string(s):"))
fullmes_received = False
checksum = "00000000"
binary_num = []
target_server = ""
binary_string = ""
flag = ""

if user_input == 'i':
    bs = 8
    num = int(input("Enter a number, no spaces:"))
    host = ""
    binaryThing(num)
    for x in binary_num:
        binary_string += str(x)
    host = binary_string

else:
    bs = 1          
    host = input("Enter a message, no spaces:")

while not fullmes_received:
    if len(target_server) == len(host):
            fullmes_received = True
            print ("Completed.")
    else:
        checksum = getchecksum()
        if not checksum == "11111111":
            print ('Error, attempting again..')
            reSend()
            bs = bs * 2
        else:
            target_server = send2Server()
            bs = bs * 2        

        
