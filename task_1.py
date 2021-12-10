import typing


def get_first_array_elements_not_in_second_array(
    first_array: typing.List,
    second_array: typing.List,
):
    """
    Get elements from first array does not exists in second array
    Complexity:
        O(len(first_array) + len(second_array)) if no unhashable type values in arrays
        O(len(first_array) * len(second_array)) if unhashable type values in arrays
    :param first_array:
    :param second_array:
    :return:
    """
    try:
        return set(first_array) - set(second_array)
    except TypeError:
        result = []
        for element in first_array:
            if element not in second_array:
                result.append(element)
        return result


if __name__ == '__main__':
    # Without unhashable types
    first_list = [1, 2, '3', '4', 5]
    second_list = ['1', 2, 3, '4', 5]

    print(
        get_first_array_elements_not_in_second_array(first_list, second_list)
    )

    # With unhashable types
    first_list = [{1: 2}, {'3': '4'}, 6, {5: '6'}]
    second_list = [{'1': 2}, 3, {'4': 5}, {'3': '4'}]

    print(
        get_first_array_elements_not_in_second_array(first_list, second_list)
    )
