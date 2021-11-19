def main():
    # write your code below this line
    mystring = []
    loop = 'y'
    while loop == 'y':
        x = input('Enter a String:\n')
        if x == '':
            print(mystring[2])
            loop = 'n'
        else:
            mystring.append(x)


if __name__ == '__main__':
    main()
