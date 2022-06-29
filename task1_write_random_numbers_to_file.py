import math
import random


def fill_file_random_numbers(file_name, numbers_count=100, max_line_length=10):
    file_random_numbers = open(file_name, 'w')
    try:
        lines_count = math.ceil(numbers_count / max_line_length)
    except ZeroDivisionError:
        print('max_line_length cannot be equal to 0')
        lines_count = 0

    if lines_count:
        for _ in range(lines_count):
            for _ in range(max_line_length):
                if numbers_count == 0:
                    break
                else:
                    file_random_numbers.write(str(random.randint(0, 20)) + ' ')
                    numbers_count -= 1
            if numbers_count == 0:
                break
            else:
                file_random_numbers.write('\n')
        file_random_numbers.close()


# TESTS
def test_fill_file_random_numbers_items_count():
    file_name = 'test_fill_file_random_numbers_items_count.txt'
    expected_items_count = random.randint(0, 1000)
    fill_file_random_numbers(file_name, numbers_count=expected_items_count)
    with open(file_name, 'r') as file:
        actual_items = file.read()
    actual_items = actual_items.split(" ")
    actual_items.pop()
    actual_items_count = len(actual_items)
    print(f'expected_items_count: {expected_items_count}, actual_items_count: {actual_items_count}')
    assert expected_items_count == actual_items_count


def test_fill_file_random_numbers_max_line_length():
    file_name = 'test_fill_file_random_numbers_max_line_length.txt'
    expected_line_length = random.randint(0, 10)
    fill_file_random_numbers(file_name, max_line_length=expected_line_length)
    file_lines = []
    with open(file_name, 'r') as file:
        for line in file:
            file_lines.append(line)

    actual_length_list = []
    for line_item in file_lines:
        line_item = line_item.split(' ')
        line_item.pop()
        actual_length_list.append(len(line_item))

    print(expected_line_length)
    print(actual_length_list)
    actual_length_list.pop()
    for actual_length in actual_length_list:
        assert expected_line_length == actual_length


def test_fill_file_random_numbers_file_not_empty():
    file_name = 'test_fill_file_random_numbers_file_not_empty.txt'
    fill_file_random_numbers(file_name)
    with open(file_name, 'r') as file:
        actual_items = file.read()
    assert len(actual_items) > 0


def test_fill_file_random_numbers_max_line_length_cannot_be_zero():
    file_name = 'test_fill_file_random_numbers_max_line_length_cannot_be_zero.txt'
    fill_file_random_numbers(file_name, max_line_length=0)
    with open(file_name, 'r') as file:
        actual_items = file.read()
    assert len(actual_items) == 0
