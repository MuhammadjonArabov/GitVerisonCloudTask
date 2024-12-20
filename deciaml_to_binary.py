def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

if __name__ == "__main__":
    number = int(input("10-lik sonni kiriting: "))
    print(f"2-lik tizimda: {decimal_to_binary(number)}")
