
def get_sum_of_even_divisor_results(input: str, cell_delim: str ="\t", row_delim: str = "\n") -> int:
    """
    Each row should have exactly one set of numbers that divide evenly.
    Get the sum of each row's result of this even division.
    :param input: The filename of an appropriately-formatted input file.
    :param cell_delim: The delimeter used on the row-level to separate the values.
    :param row_delim: The delimeter used on the table-level to separate rows.
    :return: The accumulation of row-level results.
    """
    accumulator = 0
    # Open input file
    with open(input, 'r') as f:
        for line in f:
            # Trim the newline character, then split the string by the tabs present in input, then map each string as an int.
            row = sorted(list(map(int, line.rstrip(row_delim).split(cell_delim))))
            val_found = False
            for idx, cell in enumerate(row):
                if val_found:
                    break
                for idx2, cell2 in enumerate(row):
                    if idx == idx2:
                        # Don't compare identical cells to avoid always finding self / self = 1
                        continue
                    if cell % cell2 == 0:
                        # Found evenly divisible value, increment accumulator and go to next row.
                        accumulator += int(cell / cell2)
                        val_found = True
                        break
    return accumulator


if __name__ == "__main__":
    example_result = get_sum_of_even_divisor_results("example_input_part_two.txt", cell_delim=" ")
    assert example_result == 9
    print(get_sum_of_even_divisor_results("input.txt"))

