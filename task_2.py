import typing


def remove_zeros_from_list(input_array: typing.List) -> typing.List:
    """
    Remove zeroes from list without allocating extra memory
    :param input_array:
    :return: array without zeroes
    """
    non_zero_idx = 0
    for idx in range(len(input_array)):
        if input_array[idx] != 0:
            input_array[non_zero_idx] = input_array[idx]
            non_zero_idx += 1

    return input_array[:non_zero_idx]


if __name__ == '__main__':
    print(
        remove_zeros_from_list([0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0])
    )

