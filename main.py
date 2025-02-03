def return_or_exchange():
    choice = None
    while choice is None:
        choice = input("Do you want to return or exchange a product? ")
        if choice.lower() != "exchange" or "return":
            print('Invalid Input. Please choose between "exchange" and "return".')
            choice = None;
    return choice
