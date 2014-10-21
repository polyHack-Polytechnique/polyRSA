#!/usr/bin/python3

# calculate modular multiplicative inverse 
def calculate_d(e, phi):
    u = [1, 0, phi]
    v = [0, 1, e]
    while v[2] != 0:    
        q = u[2] // v[2]
        temp1 = u[0] - q * v[0]
        temp2 = u[1] - q * v[1]
        temp3 = u[2] - q * v[2]
        u[0] = v[0]
        u[1] = v[1]
        u[2] = v[2]
        v[0] = temp1
        v[1] = temp2
        v[2] = temp3
    if (u[1] < 0):
        return (u[1] + phi)
    else:
        return u[1]

# turn string into int : "AAAA" -> int(0x41414141)
def string_to_int(string_message):
    hex_str_message = ""
    for letter in string_message:
        hex_str_message += str(hex(ord(letter)))[2:4]
    int_message = int(hex_str_message,16)
    return(int_message)

# turn int into string : (0x41414141) -> "AAAA"
def int_to_string(int_message):
    hex_str_message = str(hex(int_message))[2:]
    string_message = ""
    for i in range(0,len(hex_str_message),2):
        hex_char =  int(hex_str_message[i:i+2],16)
        string_message += chr(hex_char)
    return string_message

# encrypt plaintext message m
def encrypt(n, e, m):
    max_length = ((len(str(n))-1) // 2) + 1
    if len(m) > max_length:  # make sure message isn't too long for keys
        return None
    m_int = string_to_int(m)
    c = pow(m_int,e,n)
    return c

# decrypt cyphertext message c
def decrypt(n, d, c):
    m_int = pow(c,d,n)
    m = int_to_string(m_int)
    return m

# generate keys
def generate_keys(p, q):
    e = pow(2,16) + 1
    n = p*q
    phi = n - (p + q - 1)
    d = calculate_d(e, phi)
    public_key = (n, e)
    private_key = (n, d)
    return (public_key, private_key)

# validates that keys haven't been used before (enhanced-security super-premium feature)
def is_n_unique(public_key):
    for key in open("/tmp/polyRSA_public.keys", "r").readlines():
        if public_key == key.strip():
            # key not unique!
            return False
    # unique key, update file
    with open("/tmp/polyRSA_public.keys", "a") as public_keys_file:
        public_keys_file.write("%s\n" % public_key)
    return True
