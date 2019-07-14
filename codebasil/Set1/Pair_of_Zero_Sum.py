
# You're given an array of integers. Write a function that returns a pair of numbers such that they sum up to zero.
#
# You can assume there will be exactly 1 solution. You can't use the same number twice.
#
# Example:
#
# Array of integers is [2, 7, 9, -2].
# The pair that sums up to 0 is (2, -2).

working_list = []
result_set = []

def main():
    # Request the input.  
    input_string = input("Enter a list of whole numbers seperated by commas.")
    # Check to make sure we have numbers to work with.
    for input_item in input_string.split(sep=","):
        try:
            int(input_item)
        except:
            print(f"{input_item} does not appear to be an integer - skipping it.")
        else:
            working_list.append(int(input_item))
    # Loop through the list of numbers.  POP one off the end and check
    #    it against the remaining numbers in the list.
    while(len(working_list) > 0):
        my_number = working_list.pop()
        for number in working_list:
            if my_number + number == 0:
                result_set.append([my_number,number])
    # See if we got one result.  If so print it otherwise print an error.
    if len(result_set) == 1:
        print(f"These numbers in the set add up to 0: {result_set[0][0]} , {result_set[0][1]}")
    elif len(result_set) == 0:
        print("I couldn't find a pair of numbers that equal 0")
    else:
        print("Something went wrong.  I found more than 2 sets that added to 0.  Please check the number list.")

if __name__ == '__main__':
    main()

