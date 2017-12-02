
def calculate_checksum(input: str, cell_delim: str ="\t", row_delim: str = "\n") -> int:
    """
    Calculate the checksum, which is an accumulation of each row's sum of max and min.
    :param input: The filename of an appropriately-formatted input file.
    :param cell_delim: The delimeter used on the row-level to separate the values.
    :param row_delim: The delimeter used on the table-level to separate rows.
    :return: The checksum for the file as an int.
    """
    accumulator = 0
    # Open input file
    with open(input, 'r') as f:
        for line in f:
            # Trim the newline character, then split the string by the tabs present in input, then map each string as an int.
            row = list(map(int, line.rstrip(row_delim).split(cell_delim)))
            accumulator += max(row) - min(row)
    return accumulator


if __name__ == "__main__":
    example_result = calculate_checksum("example_input.txt", cell_delim=" ")
    assert example_result == 18

    print(calculate_checksum("input.txt"))

