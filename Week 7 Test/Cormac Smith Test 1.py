def kaprekar(upper):            # Checks all the numbers to see if they are Kaprekars or not
    n = 10
    list1 = []

    while n <= upper:           # while loop to make sure it goes through all number from 10 to the users input
        m = n*n
        m = str(m)              # turns into string to get length of number
        l = len(m)              # getting length as an int

        if l % 2 == 0:          # checks if number is an even length or not (ie 2,4,6,8 etc in length)
            h = l/2             # divide length in half to split up the number
            h = int(h)          # turn back into an integer for addition
            p1 = int(m[0:h])    # Takes first half
            p2 = int(m[h:])     # Takes second half

            if p1 + p2 != n:    # Checks if adding unequally works (ie: Numbers like 4879)
                l = l-1
                h = l / 2
                h = int(h)
                p1 = int(m[0:h])
                p2 = int(m[h:])

        if l % 2 != 0:          # for numbers which have an odd length
            l = l+1
            h = l/2
            h = int(h)
            p1 = int(m[0:h])
            p2 = int(m[h:])

            if p1 + p2 != n:    # Checks if adding them a different way works (ie: numbers like 2223)
                l = l-1
                h = l / 2
                h = int(h)
                p1 = int(m[0:h])
                p2 = int(m[h:])

        if p1 + p2 == n:        # If the two numbers added finally do equal n, add them to the list
            list1.append(n)

        n = n+1                 # increments n to move onto next number

    display(list1)              # Calls display and passes the list to display


def display(list1):             # Used to print the list of numbers that are Kaprekar
    print(list1)


upper_limit = int(input("Enter an upper limit (inclusive):"))       # Asks user to input upper limit (inclusive)

kaprekar(upper_limit)           # goes to function kaprekar

