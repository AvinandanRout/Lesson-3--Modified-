# importing the module
import sys


def initial_phonebook():
    rows, cols = int(imput("Please enter initial number of contacts: "))


    #We are cllecting the initial number of contacts the user wants to have in the 

    any.

           phone_book = []
           print(phone_book)
           for i in range(rows):
                   print("\nEnter contact %d details in the following order(ONLY):" % (i+1))
                   print("NOTE: * indicates mandatory fields")


print("............................................................................")
               temp = []
               for j in range(cols):
        if j == 0: 
                 temp.append(str(input("Enter name*: ")))
                 if temp[j] == '' or temp[j] == ' ':
                    sys.exit(
                        "Name is a mandatory field. Process exiting due to blank field...")
                    if j == 1:
                            tem.append(int(input("Enter number")))

                            if j == 2:
                                    temp.append(str(input("Enter e-mail address:")))

                                    if temp[j] == ' ' or temp[j] == ' ':
                                            temp[j] = None


                                    if j == 3:
                                            temp.append(str(input("Enter date of birth(dd/mm/yy): ")))

                                            if temp[j] == '' or temp[j] == ' ':
                                                    temp[j] = None
                                            if j == 4:
                                                    temp.append(
                                                            str(input("Enter catagory(Famly/Friends/Work/Others)"))

                                                            if temp[j] == "" or temp[j] == ' ':
                                                                    temp[j] = None
                                                    )
                                                    phone_book.append(temp)
                                    phone_book

                                             print(phone_book)
                                             return phone_book 
                                                                                                
        