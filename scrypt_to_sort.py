from os import listdir, mkdir, rename
from os.path import isfile, join, isdir

path = 'Downloads'

file_resolutions = set()
files_in_dir = [(f, f.split('.')[-1]) for f in listdir(path) if isfile(join(path, f)) and len(f.split('.')) > 1]

for (name, res) in files_in_dir:
    if res not in file_resolutions:
        file_resolutions.add(res)
        try:
            mkdir(join(path,res))
            print('Created directory: ', res)
        except FileExistsError:
            pass
        except Exception as e:
            print('Error with create directory: ', e)

    try:
        rename(join(path, name), join(path, res, name))
        print(f'File ({name}) has been moved form {path} to {join(path, res)}')
    except Exception as e:
        print('Error with moved file: ', e)

print('DONE!')
