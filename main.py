#!/usr/bin/env python3

"""
For a given atomic number print the electron configuration.
"""

from sys import argv

ordered_subshells = [
    '1s',
    '2s',
    '2p', '3s',
    '3p', '4s',
    '3d', '4p', '5s',
    '4d', '5p', '6s',
    '4f', '5d', '6p', '7s',
    '5f', '6d', '7p',
    '6f', '7d',
    '7f'
]

subshell_orbital_count = {
    's': 1,
    'p': 3,
    'd': 5,
    'f': 7
}

def main():
    atomic_number = get_atomic_number()
    if atomic_number == 0:
        print_usage_message()
        exit(1)

    electron_configuration = get_electron_configuration(atomic_number)

    print(electron_configuration)


def get_atomic_number():
    atomic_number = 0

    try:
        if len(argv) == 1:
            atomic_number = int(input())
        elif len(argv) == 2:
            atomic_number = int(argv[1])
    except ValueError:
        print_non_integer_error_message()
        return atomic_number

    if atomic_number < 1 or atomic_number > 156:
        print_incorrect_range_message()
        atomic_number = 0

    return atomic_number


def print_usage_message():
    print(f'Usage:\n\t./{argv[0]} [atomic_number]')


def print_non_integer_error_message():
        print('Error:\n\tInput must be an integer')


def print_incorrect_range_message():
        print('Error:\n\tInput must be in range [1, 156]')


def get_electron_configuration(atomic_number):
    electron_configuration = ''
    remaining_electrons = atomic_number
    current_subshell_index = 0

    while current_subshell_index < len(ordered_subshells):
        current_subshell = ordered_subshells[current_subshell_index]
        current_subshell_type = current_subshell[1]
        current_subshell_orbital_count = \
                subshell_orbital_count[current_subshell_type]

        if remaining_electrons < 2 * current_subshell_orbital_count:
            break

        electron_configuration += current_subshell + ': '
        electron_configuration += '2' * current_subshell_orbital_count + '\n'
        remaining_electrons -= 2 * current_subshell_orbital_count

        current_subshell_index += 1

    if remaining_electrons == 0:
        return electron_configuration[:-1]

    model = [0] * current_subshell_orbital_count
    for k in range(2):
        for i in range(current_subshell_orbital_count):
            if remaining_electrons > 0:
                model[i] += 1
                remaining_electrons -= 1

    electron_configuration += current_subshell + ': '
    electron_configuration += ''.join(map(str, model))

    return electron_configuration


def get_max_electron_count():
    max_electron_count = 0
    for subshell in ordered_subshells:
        max_electron_count += subshell_orbital_count[subshell[1]] * 2
    return max_electron_count


if __name__ == '__main__':
    main()
