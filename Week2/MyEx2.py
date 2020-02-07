def read_file(path):
    with open(path) as file_object:
        lst = []
        for line in file_object:
            print(line)
            lst.append(line)
        return lst


# 1.A. def print_file_content(file) that can print content of a csv file to the console
# read_file('dat4sem2020spring-python-master/teams.csv')

filename = 'dat4sem2020spring-python-master/IO_tests.txt'
list_of_tuples = ("Nikolaj", "Jon", "Lars")
list_of_strings = ["Matias", "Karl", "Ulrik"]


def write_data(path, lst):
    with open(filename, 'a') as file_object:
        for var in lst:
            file_object.write(var)


# 1.B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
#write_tuple(filename, list_of_tuples)
# 1.B.a rewrite the function so that it gets an arbitrary number of strings instead of a list
#write_tuple(filename, list_of_strings)

# 1.C. def read_csv(input_file) that take a csv file and read each row into a list
#write_data(filename, read_file('dat4sem2020spring-python-master/teams.csv'))

# 2. Add a functionality so that the file can be called from cli with 2 arguments
#       A: path to csv file
#       B: an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.

import argparse
import sys

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Ex2 read/write")
    parser.add_argument("path", help="Path to csv file")
    parser.add_argument("--file", help="Path to file that it will write to")
    args = parser.parse_args()

    if args.file is None:
        read_file(args.path)
    else:
        write_data(args.file, read_file(args.path))

