#  Sorts files in programs dir by extensions(.exe, .pdf, ...) to sorted dir
#  IMPROVE?
#  1. to differentiate versions of the same file

import os
import shutil


def sort_files():
    root_path = os.getcwd()
    root_files = os.listdir(root_path)
    #  check for sorted folder
    if 'sorted' not in root_files:
        os.makedirs('sorted')
    os.chdir(root_path + "\\sorted\\")
    sorted_path = os.getcwd()
    sorted_files = os.listdir(sorted_path)
    for file in root_files:
        file_ext = file.split('.')
        print("file: " + file)
        print("file_ext: " + str(file_ext))
        print("file_ext[-1]: " + file_ext[-1])
        #  check that we have a file with ext and not our script
        if len(file_ext) > 1 and file != 'sorting_your_shitpile.py':
            #  check that we create new subfolder
            if file_ext[-1] not in sorted_files:
                os.makedirs(file_ext[-1])
                print('Made directory: ' + str(file_ext[-1]))
            # check that we're not  moving same file
            # !!! improve it to differentiate versions of the same file
            if file not in os.listdir(sorted_path + '\\' + str(file_ext[-1])):
                shutil.move(root_path + '\\' + file, sorted_path + '\\' + str(file_ext[-1]))
                print('Moved ' + file)
        # shutil.move(file, new_dir)


sort_files()
