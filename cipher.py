#Caesar Cipher Challenge

cipher = {
    "a" : "f", "b" : "g", "c" : "h", "d" : "i", "e" : "j", "f" : "k",
    "g" : "l", "h" : "m", "i" : "n", "j" : "o", "k" : "p", "l" : "q",
    "m" : "r", "n" : "s", "o" : "t", "p" : "u", "q" : "v", "r" : "w",
    "s" : "x", "t" : "y", "u" : "z", "v" : "a", "w" : "b", "x" : "c",
    "y" : "d", "z" : "e",

    "A" : "F", "B" : "G", "C" : "H", "D" : "I", "E" : "J", "F" : "K",
    "G" : "L", "H" : "M", "I" : "N", "J" : "O", "K" : "P", "L" : "Q",
    "M" : "R", "N" : "S", "O" : "T", "P" : "U", "Q" : "V", "R" : "W",
    "S" : "X", "T" : "Y", "U" : "Z", "V" : "A", "W" : "B", "X" : "C",
    "Y" : "D", "Z" : "E"
}

plain_text = input("Please enter a sentence to be encrypted:")

result = ''
for letter in plain_text:
    if letter in cipher:
        result = result + cipher[letter]
    else:
        result = result + letter
        
print("Your encrypted sentence is:", result)
