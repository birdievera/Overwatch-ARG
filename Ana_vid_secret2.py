# numbers from http://pastebin.com/21eE1zLi

num = "65 76 2E 2E 2E 7B 76 20 66 62 72 20 63 7E 72 79 72 20 7B 76 20 7E 79 71 \
78 65 7A 76 74 7E D4 A4 79 2C 20 63 7E 72 79 72 20 72 7B 20 67 78 73 72 65 2E \
2E 2E 7B 76 20 66 62 72 20 63 7E 72 79 72 20 7B 76 20 7E 79 71 78 65 7A 76 74 \
7E 04 A4 79 2C 20 63 7E 72 79 72 20 72 7B 20 67 78 73 72 65 2E 2E 2E 7B 76 20 \
66 62 72 20 63 7E 72 79 72 20 7B 76 20 7E 79 71 78 65 7A 76 74 7E 04 A4 79 2C \
20 63 7E 72 79 72 20 72 7B 20 67 78 73 72 65 2E 2E 2E 7B 76 20 66 62 72 20 63 \
7E 72 79 72 20 7B 76 20 7E 79 71 78 65 7A 76 74 7E 04 A4 79 2C 20 63 7E 72 79 \
72 20 72 7B 20 67 78 73 72 65 2E 2E 2E"
#const = 23

# convert HEX to ASCII
ascii = [chr(int(n, 16)) for n in num.split(' ')]

for const in range(0, 30): 
    
    print "const: " + str(const)
    
    # XOR const
    string = [ord(n)^const if n != " " else ord(n) for n in ascii]
    
    decoded = ''.join((chr(s) for s in string))
    print (decoded)