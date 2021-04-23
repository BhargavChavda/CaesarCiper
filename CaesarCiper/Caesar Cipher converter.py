shift = 4

text = input("Enter the text: ")
encry = ""

for x in text:
    if x.isupper():
        ccode = ord(x)
        cindex = ord(x)-ord("A")

        newindex = (cindex + shift)%26

        newcode = newindex+ord("A")
        newchar = chr(newcode)

        encry = encry + newchar

else:
    if x.islower():
        clcode = ord(x)
        clindex = ord(x)-ord("a")

        clnindex = (clindex + shift)%26

        nlcode = clnindex+ord("a")
        nchar = chr(nlcode)

        encry = encry + nchar

    print("Text", text)
    print("Encryption: " + encry)
    