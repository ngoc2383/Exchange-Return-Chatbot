'''
def unpack_data(data):
    product_names = []
    product_ids = []
    product_dates = []
    file = open(data, 'r')
    for line in file:
        line = line.split(' - ')
        product_names.append(line[0]).strip()
        product_ids.append(line[1]).strip()
        product_dates.append(line[2]).strip()
    return product_names, product_ids, product_dates
'''     

def directions():
    print("\n=====================================\n")
    print("Hello. Please read through this manual for how to use the chatbot.\n  1. The chatbot is designed to help you return or exchange a product.\n  2. You will be asked to provide the product ID, the date you bought the product, and the reason for returning or exchanging the product.\n  3. Please provide the information as accurately as possible.\n  4. If you need help at any point, please type '1' to get directions.\n  5. If you are ready to proceed, please type 'return' or 'exchange' to get started.\n")
    print("Commands: \n  1. '1' - Get directions\n  2. 'return' - Return a product\n  3. 'exchange' - Exchange a product\n  4. 'exit' - Exit the chatbot")
    print("\n=====================================\n")

def return_or_exchange():
    choice = None
    while choice is None:
        choice = str(input("Do you want to return or exchange a product?(1 for help) ")).strip()
        if choice == "1":
            directions()
            choice = None
        elif choice.lower() == "exit":
            print("Thank you for using the chatbot.")
            exit()
        elif choice.lower() == "exchange" or choice.lower() == "return":
            return choice
        else:
            print('Invalid Input. Please choose between "exchange" and "return".\n')
            choice = None

def product_id():
    product_id = None
    while product_id is None:
        product_id = str(input("Please enter the product ID: ")).strip()
        if len(product_id) == 6:
            print("Valid ID.\n")
            return product_id
        else:
            print("Invalid product ID. Product ID must be 6 characters.\n")
            product_id = None

def bought_date():
    bought_date = None
    while bought_date is None:
        bought_date = str(input("Please enter the date you bought the product: ")).strip()
        if len(bought_date) == 8:
            print("Valid Date.\n")
            return bought_date
        else:
            print("Invalid date. Date must be in MMDDYYYY format.\n")
            bought_date = None

def return_exchange_reason(choice):
    reason = None
    while reason is None:
        reason = str(input(f"Please enter the reason for {choice} the product: ")).strip()
        if len(reason) > 0:
            print("Thank you for your response.\n")
            return reason
        else:
            print("Invalid reason. Please enter at least one character.\n")
            reason = None

def clarify(choice, product_id, bought_date, reason):
    print('Please review the information you have provided:\n')
    print(f' * Return/Exchange: {choice}')
    print(f' * Product ID: {product_id}')
    # print(f'Product: {product_name}')
    print(f' * Bought Date: {bought_date}')
    print(f' * Reason: {reason}')
    clarification = None
    while clarification is None:
        clarification = str(input("\nDoes all the information look correct? ")).strip()
        if clarification.lower() == "yes" or clarification.lower() == "y":
            return True
        elif clarification.lower() == "no" or clarification.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            clarification = None

def main():
    while True:
        print("\n=====================================\n")
        print("Welcome to the chatbot.")
        print()
        # unpack_data("data.txt")
        userchoice = return_or_exchange()
        prod_id = product_id()
        # prod_name = product_name(prod_id)
        date = bought_date()
        reason = return_exchange_reason(userchoice)
        print("\n=====================================\n")
        clarification = clarify(userchoice, prod_id, date, reason)
        if clarification == True:
            print("Thank you for your response. Your request has been submitted.")
            break
        else:
            print("\nPlease re-enter the information.")
main()


'''
Highlights:
 - Purpose: to help customers return or exchange a product.
 - Input: product ID, date bought, reason for return/exchange.
 - Output: confirmation of request and submission.
 - Functions: return_or_exchange, product_id, bought_date, return_exchange_reason, clarify.
 - Most challenging: edge cases problems and improper loop
 - Possible additional function: data.txt as the store inventory --> make experience more realistic.
'''