Title = '''

(  ____ \(  ___  )(  ____ \(  ____ \(  ___  )(  ____ )
| (    \/| (   ) || (    \/| (    \/| (   ) || (    )|
| |      | (___) || (__    | (_____ | (___) || (____)|
| |      |  ___  ||  __)   (_____  )|  ___  ||     __)
| |      | (   ) || (            ) || (   ) || (\ (   
| (____/\| )   ( || (____/\/\____) || )   ( || ) \ \__
(_______/|/     \|(_______/\_______)|/     \||/   \__/
                                                      
 _______ _________ _______           _______  _______ 
(  ____ \\__   __/(  ____ )|\     /|(  ____ \(  ____ )
| (    \/   ) (   | (    )|| )   ( || (    \/| (    )|
| |         | |   | (____)|| (___) || (__    | (____)|
| |         | |   |  _____)|  ___  ||  __)   |     __)
| |         | |   | (      | (   ) || (      | (\ (   
| (____/\___) (___| )      | )   ( || (____/\| ) \ \__
(_______/\_______/|/       |/     \|(_______/|/   \__/
                                                      '''
print(Title)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message_input = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO: The functions 
def encrypt(message_input):
    result = ""
    for m in message_input:
        for i in range(len(alphabet)):
            if m == alphabet[i]:
                result += alphabet[i+shift-len(alphabet)]
    print(result)

def decrypt(message_input):
    result = ""
    for m in message_input:
        for j in range(len(alphabet)):
            if m == alphabet[j]:
                result += alphabet[j-shift]
    print(result)
    
'''if mode == "encode":
    encrypt(message_input)
elif mode == "decode":
    decrypt(message_input)'''

keep_going = "yes"
  
while keep_going == "yes" :
    if mode == "encode":
        print("here's the encoded result : ")
        encrypt(message_input)
    elif mode == "decode":
        print("Here's the decoded result : ")
        decrypt(message_input)
    keep_going = input("Type 'yes' if you want to go again. Otherwise no.").lower()
