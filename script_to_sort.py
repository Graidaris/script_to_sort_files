from os import listdir, mkdir, rename
from os.path import isfile, join, isdir

print("Path to sort: ")
path = input()

file_format = set()
files_in_dir = [(f, f.split('.')[-1]) for f in listdir(path) if isfile(join(path, f)) and len(f.split('.')) > 1]

for (name_of_file, format_of_file) in files_in_dir:
    if format_of_file not in file_format:
        file_format.add(format_of_file)
        try:
            mkdir(join(path,format_of_file))
            print('Created directory: ', format_of_file)
        except FileExistsError:
            pass
        except Exception as e:
            print('Error with create directory: ', e)

    try:
        rename(join(path, name_of_file), join(path, format_of_file, name_of_file))
        print(f'File ({name_of_file}) has been moved form {path} to {join(path, format_of_file)}')
    except Exception as e:
        print('Error with moved file: ', e)

print('Complete!')
