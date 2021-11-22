def increment_to(a: int, b: int):
    for i in range(a, b):
        print(i)


def decrement_and_print_even(a: int, b: int):
    '''
    prints all even numbers between max and min
    '''
    for i in range(a, b, -1):
        if i % 2 != 0:
            print(i);


def loop_while_number():
    while True:
        try:
            number = int(input("Enter a number between 1 and 10: "));
            if (number >= 1 and number <= 10):
                print(number);
                break;
            else:
                print("The number is not between 1 and 10");
        except:
            print("invalid input");
            
            
def print_string_by_char(string: str):
    for i in string:
        print(i);
        
def print_number_with_steps(a: int, b: int, step: int):
    for i in range(a+1, b-1, step):
        print(i);
        
        
def print_from_to_except(a: int, b: int, except_number: int):
    for i in range(a, b):
        if i != except_number:
            print(i);        