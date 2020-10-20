# CSC 217 - Assignment Five - Searchin' and Sortin'
# Programmer: Connor McCloskey
# Date created: 7/20/2020
# Date of final update: 7/21/2020


# Write-up -------------------------------------------------------------------------------------------------------------
"""
Well, I had to change a number of things from my original design, but here it is!

1) Variables & imports - Shock! Call the newspapers! I have something other than just a boolean for menu loops this
time! I included the 'random' library to use the randint function
2) Functions - Contains all requested functions, plus a few extras to either help them along or complete other tasks
3) Main program - As always, it contains the main program loop. This time, the main menu looks (slightly) more usable!
It also contains a few things to properly call and use each function.
"""
# --------------------------------------------------------------------------------------------------------------------//

# Variables & Imports --------------------------------------------------------------------------------------------------
# Import random for randint, which we'll use to generate random numbers for some of our arrays
import random
# Boolean for controlling menu loops
done = False
# --------------------------------------------------------------------------------------------------------------------//


# Functions ------------------------------------------------------------------------------------------------------------
# Ye olde radix function
# @param j MUST start at 0 in initial call
# After some additional reading up on radix functions, it sounds like most of them actually start at the hundredths
# place and work backward, but per the instructions, this one does the opposite (goes from left -> right)
def radix(array, j):
    # base case - if we've checked all digits, or if the array is empty, return
    if j == 3 or len(array) == 0:
        return

    # Auxiliary lists
    array0 = []
    array1 = []
    array2 = []
    array3 = []
    array4 = []
    array5 = []
    array6 = []
    array7 = []
    array8 = []
    array9 = []

    # For loop - check the digit at j at the element in array position i, then append it to the appropriate list
    for i in range(len(array)):
        if array[i][j] == "0":
            array0.append(array[i])
        elif array[i][j] == "1":
            array1.append(array[i])
        elif array[i][j] == "2":
            array2.append(array[i])
        elif array[i][j] == "3":
            array3.append(array[i])
        elif array[i][j] == "4":
            array4.append(array[i])
        elif array[i][j] == "5":
            array5.append(array[i])
        elif array[i][j] == "6":
            array6.append(array[i])
        elif array[i][j] == "7":
            array7.append(array[i])
        elif array[i][j] == "8":
            array8.append(array[i])
        elif array[i][j] == "9":
            array9.append(array[i])

    # Clear the array so we can put sorted elements back into it
    array.clear()

    # Check our auxiliary arrays
    # If they're empty, they're irrelevant
    # Otherwise, recursive call this function to sort them
    # Then, call the append_aux function to append the newly-sorted section to the main array
    if len(array0) != 0:
        radix(array0, j+1)
        append_aux(array, array0)
    if len(array1) != 0:
        radix(array1, j+1)
        append_aux(array, array1)
    if len(array2) != 0:
        radix(array2, j + 1)
        append_aux(array, array2)
    if len(array3) != 0:
        radix(array3, j + 1)
        append_aux(array, array3)
    if len(array4) != 0:
        radix(array4, j + 1)
        append_aux(array, array4)
    if len(array5) != 0:
        radix(array5, j + 1)
        append_aux(array, array5)
    if len(array6) != 0:
        radix(array6, j + 1)
        append_aux(array, array6)
    if len(array7) != 0:
        radix(array7, j + 1)
        append_aux(array, array7)
    if len(array8) != 0:
        radix(array8, j + 1)
        append_aux(array, array8)
    if len(array9) != 0:
        radix(array9, j + 1)
        append_aux(array, array9)
    return


# Function to assist with above radix sort w/ 10 auxiliary lists
# Takes in the array and the auxiliary list, looping through the auxiliary list to append items to the main array
def append_aux(main, aux):
    for i in range(len(aux)):
        main.append(aux[i])
    return


# Ye olde radix sort with one auxiliary list
# @param j must be initialized at 2
# Unlike above list, this will start at the hundredths place and works backward
def radixRevisted(array, j):
    # Base case - if we've looked at all the digits, or if the array is empty, return
    if j < 0 or len(array) == 0:
        return
    # Variable - our auxiliary array!
    aux_array = []
    # Variable - d for digits! Represents digit (0 through 9) that we're looking for
    d = 0
    # While loop to search through all digits
    while d <= 9:
        # For loop - look through the array
        for i in range(len(array)):
            # check the digit at j at the element in array position i. If it's what we're looking for, append it to
            # our aux array
            if array[i][j] == str(d):
                aux_array.append(array[i])
        # increment the digit we want to look at
        d += 1
    # clear the array
    array.clear()
    # loop through aux array and append all items to the main array
    for index in range(len(aux_array)):
        array.append(aux_array[index])
    # recursive call
    radixRevisted(array, j-1)
    return


# binary search function
# Per the instructions, this modifies the function from the book
# The modification is really quite simple - since we increment/decrement the low/high variables to search, we will
# always know if we've failed thanks to the if/else statement. Namely, the only fail condition is if "low" is larger
# than "high." In that case, we know that our target SHOULD have come right before the high position. So, we just
# plug in the equation given to us by the instructions in our return statement (-k-1), substituting our "high" variable
# for k
def binarySearch(values, low, high, target):
    if low <= high:
        mid = (low + high) // 2

        if values[mid] == target:
            print("Target found. Position:")
            return mid
        elif values[mid] < target:
            return binarySearch(values, mid + 1, high, target)
        else:
            return binarySearch(values, low, mid - 1, target)
    else:
        print("Target not found. Position it would be at:")
        return -high-1


# Merge sort, minus the recursion!
def mergeSort(array):
    # Per the instructions, we want "chunks" of the area that are a size of a power of 2. We'll start at 1, then 2, 4,
    # etc...
    chunk = 1
    total_length = len(array)
    # So long as our chunk size isn't the size of the whole array, because that would be useless...
    while chunk < total_length:
        # Looping through the array, incrementing by the size of the chunk we want to look at
        for i in range(0, total_length, chunk*2):
            # Thanks to array slicing, we can mirror creating halves of the array, using our chunk size to help
            # figure out where these "halves" are and what they include
            first_half = array[i:i+chunk]
            second_half = array[i+chunk:i+chunk*2]
            # Once we have our halves, merge them
            merge(first_half, second_half, array, i)
        # Increment our chunk by a power of 2
        chunk = 2*chunk


# Since I found a way to "mirror" creating array of the appropriate length, we can actually now use the same merge
# function from our book, with some minor modifications. Namely, we pass in our index value (j in the book, I renamed
# a few things for my own edification/clarification) and increment from there, rather than always starting at 0. Why?
# Basically to make sure we're looking at the right place in the main array
def merge(first, second, main, i):
    iFirst = 0  # Next element to consider in the first list.
    iSecond = 0  # Next element to consider in the second list

    # As long as neither iFirst nor iSecond is past the end, move
    # the smaller element into values
    while iFirst < len(first) and iSecond < len(second):
        if first[iFirst] < second[iSecond]:
            main[i] = first[iFirst]
            iFirst = iFirst + 1
        else:
            main[i] = second[iSecond]
            iSecond = iSecond + 1

        i = i + 1

    # Note that only one of the two loops below copies entries.
    # Copy any remaining entries of the first list.
    while iFirst < len(first):
        main[i] = first[iFirst]
        iFirst = iFirst + 1
        i = i + 1

    # Copy any remaining entries of the second list.
    while iSecond < len(second):
        main[i] = second[iSecond]
        iSecond = iSecond + 1
        i = i + 1


# There's a lot of arrays in this! Lots of functions that need an array with random ints in a range of 0 to 999. So,
# here's something to speed that along!
# Takes in the requested length of the array from the user
def generate_array(length):
    i = 0
    result = []
    while i < length:
        n = random.randint(0, 999)
        result.append(n)
        i += 1
    return result
# --------------------------------------------------------------------------------------------------------------------//


# Main Program ---------------------------------------------------------------------------------------------------------
print("Yeehaw! Welcome to the 2020 McCloskey Searchin' n' Sortin' Rodeo!")
while not done:
    print("""
------------------------------------ Main Menu -------------------------------------------------------------------------
Please select a menu item by entering the corresponding letter.                                                        |
All random arrays will be 0 through 999                                                                                |
                                                                                                                       |
MAIN MENU                                                                                                              |
A) Use Radix sort with 10 auxiliary lists to sort a randomly-generated array                                           |
B) Use Radix sort with 1 auxiliary list to sort a randomly-generated array                                             |
C) Search through a randomly-generated array using binary search, returning the position your item should be at if not |
found                                                                                                                  |
D) Merge Sort a randomly-generated array without using recursion                                                       |
E) Quit program                                                                                                        |
------------------------------------------------------------------------------------------------------------------------
""")
    user_input = input("Your Selection: ")
    print("")
    # Option A - Radix w/ 10 lists - User input w/ validation, generate array, convert, function call
    if user_input.lower() == "a":
        try:
            array_length = int(input("Please enter the length of the array you'd like to generate (must be greater than zero): "))
            print("")
        except ValueError:
            print("Error. Please be sure to enter only integers when generating an array.\n")
        else:
            # Generate array and display it
            if array_length <= 0:
                print("The array length you entered is less than or equal to zero. Returning to main menu")
            else:
                array = generate_array(array_length)
                print("Original array:")
                print(array)
                print("")

                # Convert int array to string array, filling in zeroes with zfill. (What a godsend that function is!)
                for i in range(len(array)):
                    integer = array[i]
                    converted = str(integer).zfill(3)
                    array[i] = converted

                # Call function for radix sort, passing in our converted array and initializing j to 0
                # j being the digit we're looking at, our "cursor"
                radix(array, 0)

                # print the sorted array
                print("Sorted array:")
                print(array)
                print("")
    # Option B - Radix w/ one auxiliary list - User input w/ validation, generate array, convert, function call
    elif user_input.lower() == "b":
        try:
            array_length = int(input("Please enter the length of the array you'd like to generate: (must be greater than zero): "))
            print("")
        except ValueError:
            print("Error. Please be sure to enter only integers when generating an array.\n")
        else:
            if array_length <= 0:
                print("The array length you entered is less than or equal to zero. Returning to main menu")
            else:
                # Generate array and display it
                array = generate_array(array_length)
                print("Original array:")
                print(array)
                print("")

                # Convert int array to string array, filling in zeroes with zfill.
                for i in range(len(array)):
                    integer = array[i]
                    converted = str(integer).zfill(3)
                    array[i] = converted

                # Call function for radixRevisted sort, passing in our converted array and initializing j to 2
                # j being the digit we're looking at, our "cursor"
                radixRevisted(array, 2)

                # print the sorted array
                print("Sorted array:")
                print(array)
                print("")
    # Option C - binary search - User input w/ validation, generate array, sort it, function call
    elif user_input.lower() == "c":
        try:
            array_length = int(input("Please enter the length of the array you'd like to generate: (must be greater than zero: "))
            print("")
        except ValueError:
            print("Error. Please be sure to enter only integers when generating an array.\n")
        else:
            if array_length <= 0:
                print("The array length you entered is less than or equal to zero. Returning to main menu")
            else:
                array = generate_array(array_length)
                mergeSort(array)
                try:
                    target = int(input("Array generated. Please enter the integer you would like to search for: "))
                    print("")
                except ValueError:
                    print("Error. Search item must be an integer.\n")
                else:
                    low = 0
                    high = len(array)
                    print("Array:", array)
                    position = binarySearch(array, low, high, target)
                    print(position)
                    print("")
    # Option D - Merge sort w/o recursion - user input + validation, generate array, sort, print
    elif user_input.lower() == "d":
        try:
            array_length = int(input("Please enter the length of the array you'd like to generate: (must be greater than zero: "))
            print("")
        except ValueError:
            print("Error. Please be sure to enter only integers when generating an array.\n")
        else:
            if array_length <= 0:
                print("The array length you entered is less than or equal to zero. Returning to main menu")
            else:
                array = generate_array(array_length)
                print("Original array:")
                print(array)
                print("")

                mergeSort(array)

                print("Sorted array:")
                print(array)
                print("")
    # quit program
    elif user_input.lower() == "e":
        quit(0)
    # User input validation
    else:
        print("Invalid input. Please be sure to enter a letter with a corresponding menu item.\n")
# --------------------------------------------------------------------------------------------------------------------//
