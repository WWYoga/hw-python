def can_invest(X, A, B):
    if A >= X and B >= X:
        return 2
    elif A >= X:
        return "Mike"
    elif B >= X:
        return "Ivan"
    elif A + B >= X:
        return 1
    else:
        return 0

def main():
    try:
        X = int(input("enter the minimum investment amount (X): "))
        A = int(input("enter the amount of money from Mike (A): "))
        B = int(input("enter the amount of money from Ivan (B): "))

        result = can_invest(X, A, B)
        print(f"result: {result}")
    except ValueError:
        print("Enter the correct numeric values.")

if __name__ == "__main__":
    main()



