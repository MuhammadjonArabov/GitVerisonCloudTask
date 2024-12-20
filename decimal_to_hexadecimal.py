def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:].upper()

if __name__ == "__main__":
    number = int(input("10-lik sonni kiriting: "))
    print(f"16-lik tizimda: {decimal_to_hexadecimal(number)}")
