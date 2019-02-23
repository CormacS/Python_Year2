myfile = open("hnr.abc", "r")

lines = myfile.readlines()

counter = 0

for line in lines:

    if line[0] == 'X':
        print(line[2:], end="")

    if line[0] == 'T' and counter == 0:
        counter = counter + 1
        print(line[2:], end="")
    if line[0] == 'M':
        print('Time Sig:', line[2:], end="")
        counter = 0
    if line[0] == 'K':
        print("Key Sig:", line[2:])
