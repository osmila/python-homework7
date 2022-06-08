import task1_write_random_numbers_to_file

# Task 1:
# Напишите функцию для создания файла и записи в него случайных
# чисел, каждое число записывается в файл через пробел, но не больше
# 10ти чисел в строку. Всего случайных чисел должно быть 1000
print('Task 1: Create file and add 1000 random numbers:')
task1_write_random_numbers_to_file.fill_file_random_numbers('random.txt', 1000, 10)

# Tests for task 1:
print('Task 1: Tests:')
task1_write_random_numbers_to_file.test_fill_file_random_numbers_items_count()
task1_write_random_numbers_to_file.test_fill_file_random_numbers_max_line_length()
task1_write_random_numbers_to_file.test_fill_file_random_numbers_file_not_empty()
task1_write_random_numbers_to_file.test_fill_file_random_numbers_max_line_length_cannot_be_zero()

# Task 2:
# Напишите другую функцию, которая считывает первый файл и возводит каждое число в квадрат.
# Каждое полученное число должно быть дозаписано в исходный файл в таком же формате.
print('Task 2: Add sqr for random numbers in file:')
