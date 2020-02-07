from os import walk
from os import scandir


def read_folder(mypath):
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.append(dirpath)
        for dir in dirnames:
            f.append(dir)
        for file in filenames:
            f.append(file)
    return f


def write_data(path, lst):
    with open(path, 'w') as file_object:
        for var in lst:
            file_object.write(var + "\n")


def read_write():
    input_directory = "dat4sem2020spring-python-master/mylib"
    output_file = "dat4sem2020spring-python-master/IO_tests.txt"
    write_data(output_file, read_folder(input_directory))


def write_first_line(output_path, input_path):
    entries = scandir(input_path)
    with open(output_path, 'w') as output_file:
        for entry in entries:
            with open(input_path + "/" + entry.name) as file:
                output_file.write(file.readline())


def print_if_email(input_path):
    entries = scandir(input_path)
    for entry in entries:
        with open(input_path + "/" + entry.name) as file:
            for line in file:
                if "@" in line:
                    print(line)


def print_if_hashtag(input_path):
    entries = scandir(input_path)
    for entry in entries:
        with open(input_path + "/" + entry.name) as file:
            for line in file:
                if line.startswith("#"):
                    print(line)
