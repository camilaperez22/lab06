# Camila Perez
def encode(password):
    global result
    result = ""
    for i in password:
        i = int(i) + 3
        if i >= 7:
            i = i - 10
            i = str(i)
        else:
            i = str(i)
        result += i
    return result


#def decode(password, result):
   # print("The encoded password is " + result + ", and the original password is " + password + ".")

def decode(code):
    og_pwd = ""
    if len(code) == 8:
        for i in range(len(code)):
            s = int(code[i])-3
            og_pwd += str(s)
    return og_pwd

def main():
    encoding = True

    while encoding:

        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option = int(input('Please enter an option: '))
        print()

        if option == 1:
            password = input('Please enter your password: ')
            encode(password)
            print('Your password has been encoded and stored!')

        elif option == 2:
            decode(password, result)

        elif option == 3:
            break


if __name__ == "__main__":
    main()
