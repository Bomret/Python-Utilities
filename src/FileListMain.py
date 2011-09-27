'''
Created on 27.09.2011

@author: stefan
'''
import sys
import os
from com.bomret.util.terminalutils import FileLister

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("DEBUG: Please use the following syntax: end2txt.py FILEEXTENSION " +
            "DIRECTORY (optional) TXTNAME (optional).")
        sys.exit(-1)
    elif len(sys.argv) == 4:
        extension = sys.argv[1]
        directory = sys.argv[2]
        txtname = sys.argv[3]
    else:
        extension = sys.argv[1]
        directory = os.getcwd()
        txtname = 'listOfiles.txt'
    
    file_lister = FileLister()
    file_lister.find_files(txtname, directory, extension)