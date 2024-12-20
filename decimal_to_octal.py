def decimal_to_octal(decimal_number):
    return oct(decimal_number)[2:]

if __name__ == "__main__":
    number = int(input("10-lik sonni kiriting: "))
    print(f"8-lik tizimda: {decimal_to_octal(number)}")
