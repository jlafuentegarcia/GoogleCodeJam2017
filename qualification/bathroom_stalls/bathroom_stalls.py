import sys
import datetime

def read_input(file_name):
    with open(file_name, 'r') as f:
        # Remove first line
        num_cases = int(f.readline().rstrip('\n'))

        cases = list()

        for t in range(num_cases):
            n, k = list(map(int, f.readline().rstrip('\n').split(' ')))

            cases.append({'case_no': t, 'N': n, 'K': k})

    return cases


def store_output(output, output_file_name):
    with open(output_file_name, 'w') as f:
        caseno = 1
        for o in output:
            f.write("Case #" + str(caseno) + ": " + str(o[0]) + " " + str(o[1]) + '\n')
            caseno += 1


def find_stall(curr_max_hole):
    position = (curr_max_hole - 1) // 2
    return position, curr_max_hole - position - 1


def get_kth_position_and_distance(case):

    print("Solving " + str(case))

    n = case['N']
    k = case['K']

    num_holes = {n: 1}

    new_holes = (-1, -1)

    num_guys = 0

    while num_holes and num_guys < k:
        curr_max_hole = max(num_holes.keys())
        curr_num_holes = num_holes[curr_max_hole]

        new_holes = find_stall(curr_max_hole)

        num_guys += curr_num_holes

        #add the new holes
        for hole in [h for h in new_holes if h > 0]:
            num_holes[hole] = num_holes[hole] + curr_num_holes if hole in num_holes else curr_num_holes

        del num_holes[curr_max_hole]

    return max(new_holes), min(new_holes)


def main():
    t1 = datetime.datetime.now()

    print(t1)

    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'

    input = read_input(input_file_name)
    output = map(get_kth_position_and_distance, input)

    store_output(output, output_file_name)

    t2 = datetime.datetime.now()
    print (t2)

    print (t2 - t1)

if __name__ == "__main__":
    main()
