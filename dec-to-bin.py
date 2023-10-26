""" Module converts a decimal number into a binary representation and
gives a step by step explanation.
"""

def invert(binary_number: str) -> str:
    """Inverts a binary number represented as a string.

    :param binary_number: The string of the binary number to convert
    :return: The string representation of the inverted binary number
    """
    return_string = ""
    for bit in binary_number[::-1]:
        return_string += "1" if bit == "0" else "0"
    return return_string[::-1]


def add_one(binary_number: str) -> str:
    """Adds one to a string representation of a binary number

    :param binary_number: The string representation of a binary number to add one to
    :return: The string of the resulting binary number
    """
    bin_as_int = int(binary_number, 2)
    one_added = bin_as_int + 1
    return bin(one_added)[2:]

def format_binary_number(binary_number: str) -> str:
    """Formats a string of a binary number
    Example:
    In:  "10110101"
    Out: "1011 0101"

    :param binary_number: The string of the binary number
    :return: The formatted string
    """

    return_string = ""
    for i, bit in enumerate(binary_number[::-1]):
        if i % 4 == 0:
            return_string += " "
        return_string += bit
    return return_string[::-1]



def convert_dec_to_bin(number: int, bits: int) -> None:
    """Converts a decimal number to a binary representation with twos complement.

    :param number: The number to convert
    :param bits: The number of bits the converted number should have
    """
    lowest=2**(bits - 1) * -1
    highest=2**(bits - 1) - 1
    if number < lowest or number > highest:
        print(f"The number {number} is too {'high' if number > highest else 'low'} to be converted to {bits} bits.")
        return

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
