while True:
    condition1 =False
    condition2 =False
    condition3 =False

    pw1 = input("Enter password : ")

    if (len(pw1) < 8 and len(pw1) > 12):
        condition1 = True
    else:
        print("Password must be between 8 and 12 characters long")

        non_alnum =[character for character in pw1 if not character.isalnum()]
        if len(non_alnum) == 0:
            condition2 = True
        else:
            print("Password must contain at least one non-alphanumeric character")

            digit=0
            letter=0
            for character in pw1:
                if character.isdigit():
                    digit += 1
                elif character.isalpha():
                    letter += 1

            if digit > 0 and letter > 0:
                condition3 = True
            else:
                print("Password must contain at least one digit and one letter")
    if condition1 and condition2 and condition3:
        pw2 =input("enter password again: ")
        if pw1 == pw2:
              print("Password is valid")
              break
         