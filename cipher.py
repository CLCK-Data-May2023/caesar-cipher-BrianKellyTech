#Caesar Cipher Challenge

cipher = {
    "a" : "f", "b" : "g", "c" : "h", "d" : "i", "e" : "j", "f" : "k",
    "g" : "l", "h" : "m", "i" : "n", "j" : "o", "k" : "p", "l" : "q",
    "m" : "r", "n" : "s", "o" : "t", "p" : "u", "q" : "v", "r" : "w",
    "s" : "x", "t" : "y", "u" : "z", "v" : "a", "w" : "b", "x" : "c",
    "y" : "d", "z" : "e"
}

plaintext = input("Please enter a sentence: ")
plaintext = plaintext.lower()

result = ''
for letter in plaintext:
    if letter in cipher:
        result = result + cipher[letter]
    else:
        result = result + letter
        
print("The encrypted sentence is:", result)
