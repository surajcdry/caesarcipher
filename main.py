import os

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

logo = """           
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|        
"""

running = True

while running:
    method = ""
    while not (method == "encode" or method == "decode"):
        os.system('clear')
        print(logo)
        method = input("Method (encode/decode): ").lower()

    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    def encrypt(text, shift):
        new = []
        for i in text:
            if i.isalpha():
                if i.isupper():
                    temp = upper.index(i)
                    temp += shift
                    if temp > 25:
                        temp -= 26
                    new.append(upper[temp])
                else:
                    temp = lower.index(i)
                    temp += shift
                    if temp > 25:
                        temp -= 26
                    new.append(lower[temp])
            else:
                new.append(i)
        return ("".join(new))

    def decrypt(text, shift):
        new = []
        for i in text:
            if i.isalpha():
                if i.isupper():
                    temp = upper.index(i)
                    temp -= shift
                    if temp < 0:
                        temp += 26
                    new.append(upper[temp])
                else:
                    temp = lower.index(i)
                    temp -= shift
                    if temp < 0:
                        temp += 26
                    new.append(lower[temp])
            else:
                new.append(i)
        return ("".join(new))


    if method == "encode":
        message = encrypt(text, shift)
    else:
        message = decrypt(text, shift)

    print("Output:", message, "\n")

    run = input("Play again? (y/n): ").lower()
    print("")
    if run == 'n':
        running = False
