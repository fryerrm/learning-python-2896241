# Python code​​​​​​‌‌​​​‌‌​​​‌‌​‌​​‌​​‌‌​‌‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False
import os
from os import path


def file_info():
    # Your code goes here.
    # return 0
     totalBytes = 0

    filelist = os.listdir("./deps")
    print("filelist:", filelist)
    for filename in filelist:
        print("filename:", filename)
        filepathname = "./deps/"+filename
        fileprefix, file_extension = os.path.splitext(filepathname)
        print("filename and ext:", filepathname, fileprefix, file_extension)
        if file_extension == '.txt':
            file_stats = os.stat(filepathname)
            totalBytes = totalBytes + file_stats.st_size
            print("file size, running total:", file_stats.st_size, totalBytes)
        else:
            print("not right file type", filename)
    return (totalBytes)

if __name__ == "__main__":
    file_info()