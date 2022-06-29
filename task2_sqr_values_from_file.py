def calculate_lines_count_and_length(file_name):

    file_lines = []
    with open(file_name, 'r') as file:
        for line in file:
            file_lines.append(line.strip('\n'))

    line_items = []
    for line in file_lines:
        line_items.append(line.split(' '))

    for line in line_items:
        line.pop()

    max_line_items_count = len(line_items[0])
    last_line_items_count = len(line_items[-1])
    items = []
    for line in line_items:
        for item in line:
            items.append(item)

    return max_line_items_count, last_line_items_count, items


def add_sqr_values_to_existing_file(file_name, max_line_items_count, last_line_items_count, items):
    file_to_add_sqr = open(file_name, 'a')
    for _ in range(last_line_items_count, max_line_items_count):
        file_to_add_sqr.write(str((int(items.pop(0)) ** 2)) + ' ')
    file_to_add_sqr.write('\n')

    left_lines_count = len(items) // max_line_items_count

    for _ in range(left_lines_count):
        for _ in range(max_line_items_count):
            file_to_add_sqr.write(str((int(items.pop(0)) ** 2)) + ' ')
        file_to_add_sqr.write('\n')

    if len(items) > 0:
        for item in items:
            file_to_add_sqr.write(str((int(item) ** 2)) + ' ')



