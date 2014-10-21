#!/usr/bin/python3

import polyRSAlib
import polyRSArandomnumbergenerator

banner =  """
               _          ______    ______  _______ 
              | |        (_____ \  / _____)(_______)
 ____    ___  | |  _   _  _____) )( (____   _______ 
|  _ \  / _ \ | | | | | ||  __  /  \____ \ |  ___  |
| |_| || |_| || | | |_| || |  \ \  _____) )| |   | |
|  __/  \___/  \_) \__  ||_|   |_|(______/ |_|   |_|
|_|               (____/                            
Welcome! Our super software implements textbook RSA!
"""

options = """
Choose an option:
    1\t\tGenerate keys
    2\t\tEncrypt message
    3\t\tDecrypt message
    other\tExit
"""

print(banner)

choice = True
while(choice):
    print(options)
    choice = var = input("option: ")
    if choice == "1":  # Generate Keys
        """
        public key format -> "n:n_value|e:e_value"
        private key format -> "n:n_value|d:d_value"
        """
        while True:
            p = polyRSArandomnumbergenerator.get_random_number()
            q = polyRSArandomnumbergenerator.get_random_number()
            (public_key, private_key) = polyRSAlib.generate_keys(p, q)
            # generate until keys are unique
            if polyRSAlib.is_n_unique("n:%s|e:%s" % (public_key[0], public_key[1])):
                break
        print("public key : \nn:%s|e:%s" % (public_key[0], public_key[1]))
        print("private key : \nn:%s|d:%s" % (private_key[0], private_key[1]))
    elif choice == "2":  # Encrypt
        m = input("message: ")
        public_key = input("public key: ")
        n = int(public_key.split("|")[0][2:])
        e = int(public_key.split("|")[1][2:])
        c = polyRSAlib.encrypt(n, e, m)
        print("cypher text: \n%s" % c)
    elif choice == "3":  # Decrypt
        c = int(input("cypher text: "))
        private_key = input("private key: ")
        n = int(private_key.split("|")[0][2:])
        d = int(private_key.split("|")[1][2:])
        m = polyRSAlib.decrypt(n, d, c)
        print("message: \n%s" % m)
    else:  # Exit
        print("Exit (option \"%s\")" % choice)
        choice = False
