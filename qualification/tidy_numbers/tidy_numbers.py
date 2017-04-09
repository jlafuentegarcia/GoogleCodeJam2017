import sys
import datetime


def read_input(file_name):
    with open(file_name, 'r') as f:
        # Remove first line
        num_cases = int(f.readline().rstrip('\n'))

        cases = list()

        for t in range(num_cases):
            case = {'case_no': t, 'digits': list(map(int, f.readline().rstrip('\n')))}

            cases.append(case)

    return cases


def transform_to_integer(list_of_int):
    return ''.join(str(x) for x in list_of_int).lstrip('0')


def get_max_tidy_number(case):
    print(case)

    last_digit = 0
    last_increasing = -1
    first_decreasing = -1

    digits = case['digits']

    for i, digit in enumerate(digits):
        if digit > last_digit:
            last_increasing = i
        elif digit < last_digit:
            first_decreasing = i
            break
        last_digit = digit

    if first_decreasing == -1:
        res = transform_to_integer(digits)
    else:
        res = transform_to_integer(digits[:last_increasing])
        res = res + str(digits[last_increasing]-1) + ('9' * (len(digits) - last_increasing - 1))
        res = res.lstrip('0')

    return res


def store_output(output, output_file_name):
    with open(output_file_name, 'w') as f:
        caseno = 1
        for o in output:
            f.write("Case #" + str(caseno) + ": " + str(o) + '\n')
            caseno += 1


def main():
    t1 = datetime.datetime.now()
    print(t1)

    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'

    input = read_input(input_file_name)
    output = map(get_max_tidy_number, input)

    store_output(output, output_file_name)

    t2 = datetime.datetime.now()
    print(t2)

    print (t2 - t1)

if __name__ == "__main__":
    main()
