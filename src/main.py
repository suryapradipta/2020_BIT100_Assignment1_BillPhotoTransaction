# Name : I Nyoman Surya Pradipta
# Student ID : E1900344
# Date : Wednesday, 11 March 2020


# Create a main function.
def main():
    # To notify the total initial collection is 0 (zero)
    total_collection = 0

    # To call the function name display introduction message.
    displayintroductionmessage()

    # Declare a global variable inside a function,
    # and use it outside the functions.
    global name

    # (name) now be global, and can be accessed in global scope.
    name = input("What is your name? (<Enter> to quit): ")

    # By using the while loop we can execute a set of statements
    # as long as a condition is true.
    # If the variable name is not NULL the main function
    # will run the program.
    while name != "":

        # Call the getinput function after returned the value
        # and then printed in the main function.
        number_of_4r, number_of_5r = getinput()

        # The purpose of using lists is to make variables
        # more presentable.
        # Variables taken from computevalues function after returned.
        # And then call the computevalues function to displayed in the
        # main function.
        [total_number,
         price_4r,
         price_5r,
         calculation_4r_and_5r,
         delivery_cost] = computevalues(number_of_4r, number_of_5r)

        # Call the printcomputevalues function with various parameter
        # to display in the main funciton.
        printcomputedvalues(total_number,
                            number_of_4r,
                            number_of_5r,
                            price_4r,
                            price_5r,
                            calculation_4r_and_5r,
                            delivery_cost)

        # I've created the total collection condition is 0 (zero)
        # And then after a loop while the keyword
        # total collection will be added when receiving value.
        total_collection = total_transactions + total_collection

        # The (\n) keyword is to make new line.
        # Looping the name variable if the customer want to make
        # other transactions.
        name = input("\nWhat is your name? (<Enter> to quit): ")

    # The if structure in Python is run to check whether
    # this condition is true or false.
    # If this condition is true, then Python will run the statement
    # in the block condition and vice versa.
    if total_collection == 0:
        # If the condition is true.
        # If total colection = 0 will print the text.
        # The (\n) keyword is to make new line.
        print("\nNo transactions for the day.")

    # If the condition false, will call the displayfinalresult function.
    else:
        displayfinalresult(total_collection)


# This function  does not take any parameters,
# but just to display the purpose of the program
def displayintroductionmessage():
    print("The purpose of this program is to "
          "help Crystal Clear owners to calculate each customer's cost "
          "based on the number of photos 4R and 5R printed.")


# This function does not take any parameters,
# and it returns two values, representing the number of
# 4R and 5R photos to be printed
def getinput():
    # Eval () will determine the appropriate data type.
    # Create more input in one line.
    number_of_4r, number_of_5r = eval(input(
        "Enter number of 4R followed by 5R photo "
        "to print (e.g. 10, 0): "))

    # Using the Python Logical Operators in the while loop.
    while number_of_4r == 0 and number_of_5r == 0:
        print("User will not enter both zeros for "
              "the number of photos to be printed.")
        number_of_4r, number_of_5r = eval(input(
            "Enter number of 4R followed by 5R photo "
            "to print (e.g. 10, 0): "))

    # Using the Python Logical Operators in the while loop.
    while number_of_4r < 0 and number_of_5r < 0:
        print("You must enter both positive integers!")
        number_of_4r, number_of_5r = eval(input(
            "Enter number of 4R followed by 5R photo "
            "to print (e.g. 10, 0): "))

    # Using Python Comparison Operators.
    while number_of_4r < 0:
        number_of_4r = eval(input("Enter number of 4R photo: "))

    # Using Python Comparison Operators.
    while number_of_5r < 0:
        number_of_5r = eval(input("Enter number of 5R photo: "))

    # A "return" keyword is used to end the implementation
    # of the function of the call
    # and return results representing the number of 4R and 5R
    # to be printed.
    return number_of_4r, number_of_5r


# This function takes two parameters, the number of photos 4R and 5R
# to be printed.
def computevalues(number_of_4r, number_of_5r):

    # Use the keyword "global" to create multiple executable variables
    # outside of the function.
    # Because in some statements if I want to return multiple values
    # should return all if another variable,
    # it can create variables that are not needed.
    global additional_charge, total_additional_charge, \
        total_delivery_cost, total_transactions

    # Counts the number of photos 4R and 5R.
    total_number = number_of_4r + number_of_5r

    # Calculation the price of 4R and 5R photos.
    # "format ()" function is used to fix the dot number format,
    # to two digits behind the comma.
    price_4r = format(number_of_4r * 0.25, '.2f')
    price_5r = format(number_of_5r * 0.35, '.2f')

    # Calculation of the total photos price of 4R and 5R.
    calculation_4r_and_5r = format((number_of_4r * 0.25) +
                                   (number_of_5r * 0.35), '.2f')

    # Represents shipping costs for the first 50 printout.
    delivery_cost = 13.55

    # Represents the next charge for group of 10 or part.
    surcharge = 1.75

    # The if structure in Python is run to check whether
    # this condition is true or false.
    # If this condition is true, then Python will run the statement
    # in the block condition and vice versa.

    if total_number > 60:
        # calculation the number of charge
        additional_charge = int((total_number - 50) / 10 + 0.9)
        total_additional_charge = additional_charge * surcharge
        total_delivery_cost = delivery_cost + total_additional_charge
        total_transactions = (number_of_4r * 0.25) + \
                             (number_of_5r * 0.35) + \
                             (delivery_cost + total_additional_charge)

    # The backslash (\) is used to representing certain
    # whitespace characters.
    elif total_number > 50:
        additional_charge = 1
        total_additional_charge = additional_charge * surcharge
        total_delivery_cost = delivery_cost + total_additional_charge
        total_transactions = (number_of_4r * 0.25) + \
                             (number_of_5r * 0.35) + \
                             (delivery_cost + total_additional_charge)

    elif total_number <= 50:
        totalled2 = total_number - 50
        additional_charge = int(totalled2 / 10)
        total_additional_charge = additional_charge * surcharge
        total_delivery_cost = delivery_cost + total_additional_charge
        total_transactions = (number_of_4r * 0.25) + \
                             (number_of_5r * 0.35) + delivery_cost

    return [total_number,
            price_4r,
            price_5r,
            calculation_4r_and_5r,
            delivery_cost]


# This function accepts many parameters, including the value that
# has been calculated in computevalues function
def printcomputedvalues(total_number,
                        number_of_4r,
                        number_of_5r,
                        price4r,
                        price5r,
                        calculation_4r_and_5r,
                        delivery_cost):

    # The statement call the global "name" variable from main function
    # to printed in the other function
    print("Bill for", name)

    # Repetition builds up a string by multiple concatenations of a string
    # with itself (*)
    print(45 * "-")

    # In this statement call the parameters and then
    # create the formating align with the format spec align
    # such as " < " make the left, " ^ " center, " > " right align.
    print(f"{total_number:<4}{'photos':^9}{calculation_4r_and_5r:>32}")

    # Make two conditions true values based on the number photos
    # of 4R and 5R.
    if number_of_4r > 0 and number_of_5r > 0:
        print('- 'f"{number_of_4r:<4}{'4R photos @$0.25':^19}"
              f"{price4r:>10}")
        print('- 'f"{number_of_5r:<4}{'5R photos @$0.35':^19}"
              f"{price5r:>10}")
    # elif statement allows to create some conditions
    # that are of true value.
    elif number_of_4r <= 0:
        print('- 'f"{number_of_5r:<4}{'5R photos @$0.35':^19}"
              f"{price5r:>10}")
    elif number_of_5r <= 0:
        print('- 'f"{number_of_4r:<4}{'4R photos @$0.25':^19}"
              f"{price4r:>10}")

    if total_number <= 50:
        print("\nDelivery cost" f"{delivery_cost:>32}")
        print("~ First 50 or part of:" f"{delivery_cost:>13}")
    elif total_number > 50:
        print("\nDelivery cost" 
              f"{format(total_delivery_cost, '.2f'):>32}")
        print("~ First 50:" f"{delivery_cost:>24}")
        print("~ " f"{additional_charge:<3}"
              f"{'x 10 or part of @$1.75':^24}"
              f"{format(total_additional_charge, '.2f'):>6}")

    # Repetition builds up a string by multiple concatenations of a
    # string with itself (*)
    print(45 * "-")

    # "format ()" function is used to fix the dot number format,
    # to two digits behind the comma.
    print("Total $" f"{format(total_transactions, '.2f'):>38}")
    print(45 * "=")


# This function takes one parameter,
# representing the total collection of the day or an appropriate message.

def displayfinalresult(total_collection):
    print("\nTotal collection: $", format(total_collection, '.2f'))


# Execute the function:
main()
