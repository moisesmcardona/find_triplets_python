def check_array(array_size, numbers):
    for number in range(int(array_size)):
        if len(numbers) > number + 2:
            if int(numbers[number]) + int(numbers[number + 1]) + int(numbers[number + 2]) == 0:
                return 1
    return 0


def main():
    test_cases = input("Enter number of test cases: ")
    array_size = []
    numbers = []

    for i in range(int(test_cases)):
        check_array_size = input("Enter Array Size for test case " + str(i + 1) + ": ")
        while int(check_array_size) < 3:
            check_array_size = input("Must be 3 or more. Enter Array Size for test case " + str(i + 1) + ": ")
        array_size.append(check_array_size)
        check_numbers = input("Enter " + array_size[i] + " array elements: ")
        numbers_splitted = check_numbers.split(" ")
        while len(numbers_splitted) > int(array_size[i]):
            check_numbers = input("Size is incorrect. Enter " + array_size[i] + " array elements: ")
            numbers_splitted = check_numbers.split(" ")
        numbers.append(numbers_splitted)

    print("Results")

    for i in range(int(test_cases)):
        print("Test case " + str(i + 1) + ": " + str(check_array(array_size[i], numbers[i])))


main()