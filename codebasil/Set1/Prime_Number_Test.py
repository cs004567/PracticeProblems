

# Given an integer, return true if the the number is a prime number. Otherwise, return false.
#
# A prime number is a natural number greater than 1 with no positive divisors other than 1 and itself. 

working_number = None

def main():
    result_count = 0
    # Request the number to test.
    input_number = input("What whole number do you want to check?")
    try:
        int(input_number)
    except:
        print("That doesn't look right.")
    else:
        working_number = int(input_number)
    if working_number:
        for test_number in range(2,working_number):
            if working_number % test_number == 0:
                result_count += 1
    if result_count == 0:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()

