number = int(input("Enter a five-digit number: "))

units = number % 10
tens = (number // 10) % 10 
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
tens_of_thousands = (number // 10000) % 10

power_result = tens ** units

multiplied_result = power_result * hundreds

if tens_of_thousands == thousands:
    print("The difference between the number of tens of thousands and the number of thousands is zero. Division is impossible.")
else:
    final_result = multiplied_result / (tens_of_thousands - thousands)
    print(f"Result: {final_result}")