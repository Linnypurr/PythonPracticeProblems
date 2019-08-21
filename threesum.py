import math

def three_sum(list_of_numbers, number_to_sum_to):
    list_of_numbers.sort()
    end_pointer = len(list_of_numbers) - 1
    runner_pointer = 1
    beginning_pointer = 0
    isNotDone = True

    while isNotDone:
        beginning_number = list_of_numbers[beginning_pointer]
        print(beginning_number)
        runner_number = list_of_numbers[runner_pointer]
        print(runner_number)
        end_number = list_of_numbers[end_pointer]
        print(end_number)
        current_sum = beginning_number + runner_number + end_number

        if current_sum == number_to_sum_to:
            print('{} + {} + {}'.format(beginning_number, runner_number, end_number))
            isNotDone = False
        elif (beginning_number + 1) == runner_pointer and runner_pointer == (end_pointer - 1):
            print('No sum found')
            isNotDone = False
        elif runner_pointer == (end_pointer - 1) and current_sum > number_to_sum_to:
            print(' current sum greater R{} E{}'.format(runner_pointer, end_pointer))
            runner_pointer = beginning_pointer + 1
            end_pointer = end_pointer - 1
        elif runner_pointer == (end_pointer - 1) and current_sum < number_to_sum_to:
            print('current sum less R{} E{}'.format(runner_pointer, end_pointer))
            beginning_pointer = beginning_pointer + 1
            runner_pointer = beginning_pointer + 1
        else:
            runner_pointer = runner_pointer + 1


if __name__== '__main__':
    practice_list = [1, 2, 4, 7, 10, 11, 12, 14]
    three_sum(practice_list, 100)
