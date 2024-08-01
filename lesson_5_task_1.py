def describe_number(number):
    if number == 0:
        return "you entered a zero number."
    if number > 0:
        sign = "positive"
    elif number < 0:
        sign = "negative"
    if number % 2 == 0:
        parity = "even" #чётное
    else:
        parity = "uneven" #нечётное
    
    return f"you entered a {sign} {parity} number."

number = int(input("enter a number: "))
description = describe_number(number)
print(description)

