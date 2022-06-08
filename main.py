import task1_write_random_numbers_to_file

# Task 1:
# Напишите функцию для создания файла и записи в него случайных
# чисел, каждое число записывается в файл через пробел, но не больше
# 10ти чисел в строку. Всего случайных чисел должно быть 1000
print('Task 1: Create file and add 1000 random numbers:')
task1_write_random_numbers_to_file.fill_file_random_numbers('random.txt', 30, 5)

# Tests for task 1:
print('Task 1: Tests:')
task1_write_random_numbers_to_file.test_fill_file_random_numbers_items_count()
task1_write_random_numbers_to_file.test_fill_file_random_numbers_max_line_length()
task1_write_random_numbers_to_file.test_fill_file_random_numbers_file_not_empty()
task1_write_random_numbers_to_file.test_fill_file_random_numbers_max_line_length_cannot_be_zero()
