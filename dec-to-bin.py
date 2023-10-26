def invert(binary_number: str) -> str:
    return_string = ""
    for bit in binary_number[::-1]:
        return_string += "1" if bit == "0" else "0"
    return return_string[::-1]


def format_binary_number(binary_number: str) -> str:
    return_string = ""
    for i, bit in enumerate(binary_number[::-1]):
        if i % 4 == 0:
            return_string += " "
        return_string += bit
    return return_string[::-1]


def add_one(binary_number: str) -> str:
    bin_as_int = int(binary_number, 2)
    one_added = bin_as_int + 1
    return bin(one_added)[2:]


def convert_dec_to_bin(number: int, bits: int):
    is_negative = number < 0

    # to_divide has to be positive
    if not is_negative:
        to_divide = number
    else:
        to_divide = number * -1

    results = ""
    while to_divide > 0:
        remainder = to_divide % 2
        print(f"{to_divide}/2 = {int(to_divide/2)},\nRemainder: {remainder}")
        to_divide = int(to_divide / 2)
        results += str(remainder)

    # Reverse order of bits
    results = results[::-1]

    print(f"Result: {format_binary_number(results)}")
    zero_padded = "0" * (32 - len(results)) + results
    print(f"Result zero padded: {format_binary_number(zero_padded)}")
    print(f"Without formatting: {zero_padded}")

    if is_negative:
        print(f"{number} is negative. -> Invert and add one:")
        inverted = invert(zero_padded)
        print(f"Inverted: {format_binary_number(inverted)}")
        one_added = add_one(inverted)
        print(f"One added: {format_binary_number(one_added)}")
        print(f"Without formatting: {one_added}")


if __name__ == "__main__":
    num = int(input("What number do you want to convert? "))
    bits = int(input("How many bits should your binary number be? "))
    convert_dec_to_bin(num, bits)
