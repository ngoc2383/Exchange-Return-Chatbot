def directions():
    print("Hello. Please read through this manual for how to use the chatbot.\n  1. You can use this chatbot in order to complete the process of returning/ exchanging a product.\n  2. First, the chatbot would ask if you want to exchange/ return.\n  3. Then you can enter the products id to varify which item you want to return\n. 4. add more to this.....")

def return_or_exchange():
    choice = None
    while choice is None:
        choice = str(input("Do you want to return or exchange a product?(1 for help) ")).strip()
        if choice == "1":
            directions()
            choice = None
        elif choice.lower() == "exchange" or choice.lower() == "return":
            return choice
        else:
            print('Invalid Input. Please choose between "exchange" and "return".')
            choice = None
return_or_exchange()
