# numbers from http://pastebin.com/21eE1zLi

num = "2E 2E 2E 7B 76 20 66 62 72 20 63 7E 72 79 72 20 7B 76 20 7E \
79 71 78 65 7A 76 74 7E D4 A4 79 2C 20 63 7E 72 79 72 20 72 \
7B 20 67 78 73 72 65 2E 2E 2E 7B 76 20 66 62 72 20 63 7E 72 \
79 72 20 7B 76 20 7E 79 71 78 65 7A 76 74 7E D4 A4 79 2C 20 \
63 7E 72 79 72 20 72 7B 20 67 78 73 72 65 2E 2E 2E 7B 76 20 \
66 62 72 20 63 7E 72 79 72 20 7B 76 20 7E 79 71 78 65 7A 76 \
74 7E D4 A4 79 2C 20 63 7E 72 79 72 20 72 7B 20 67 78 73 72 \
65 2E 2E 2E 7B 76 20 66 62 72 20 63 7E 72 79 72 20 7B 76 20 \
7E 79 71 78 65 7A 76 74 7E D4 A4 79 2C 20 63 7E 72 79 72 20 \
72 7B 20 67 78 73 72 65 2E 2E 2E 64 78 7A 75"

num2 = "65 76 2E 2E 2E 7B 76 20 66 62 72 20 63 7E 72 79 72 20 7B 76 \
20 7E 79 71 78 65 7A 76 74 7E D4 A4 79 2C 20 63 7E 72 79 72 \
20 72 7B 20 67 78 73 72 65 2E 2E 2E 7B 76 20 66 62 72 20 63 \
7E 72 79 72 20 7B 76 20 7E 79 71 78 65 7A 76 74 7E D4 A4 79 \
2C 20 63 7E 72 79 72 20 72 7B 20 67 78 73 72 65 2E 2E 2E 7B \
76 20 66 62 72 20 63 7E 72 79 72 20 7B 76 20 7E 79 71 78 65 \
7A 76 74 7E D4 A4 79 2C 20 63 7E 72 79 72 20 72 7B 20 67 78 \
73 72 65 2E 2E 2E 7B 76 20 66 62 72 20 63 7E 72 79 72 20 7B \
76 20 7E 79 71 78 65 7A 76 74 7E D4 A4 79 2C 20 63 7E 72 79 \
72 20 72 7B 20 67 78 73 72 65 2E 2E 2E"

const = 23
# result: la que tiene la informacion; tiene el poder
# translates to "She who has the information, has the power."
# last 4 chars of num2 + first 3 chars of num1 = sombra

def xor(code):    
    # convert HEX to ASCII
    ascii = [chr(int(n, 16)) for n in code.split(' ')]
     
    # XOR const
    string = ''.join((chr(ord(n)^const) if n != " " and n != "." else n for n in ascii))
        
    return unicode(string, "utf-8")

if __name__ == "__main__":
    print ("The first frame:\n" + xor(num))
    print ("The second frame:\n" + xor(num2))
    print ("Both together:\n" + xor(num) + xor(num2))