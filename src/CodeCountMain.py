'''
Created on 27.09.2011

@author: Stefan Reichel <dev@bomret.com>
'''
import argparse
from com.bomret.util.terminalutils import CodeCounter
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count lines of code in all files with the specified extensions in a dir (and optionally its subdirs).")
    parser.add_argument('extensions', metavar='N', nargs='+', help='Extensions of the source code files you want to count lines in. If you want to count in EVERY file in the given dir, just use the asterisk (*).')
    parser.add_argument('--dir', '-d',dest='dir' , help='The directory that should be searched recursively. If not given it defaults to the current working directory.', default=os.getcwd())
    parser.add_argument('--recursive', '-r',dest='recursive', action='store_true' , help='Parse subfolders.')
    
    args = parser.parse_args()
    argvars = vars(args)
    
    extensions = argvars['extensions']
    recursive = argvars['recursive']
    dir = argvars['dir']
    
    counter = CodeCounter()

    try:
        countedFiles = counter.count_code(extensions=extensions, workdir=dir, recursive=recursive)
        totalFiles = len(countedFiles)
        totalLines = 0

        for key, value in countedFiles.iteritems():
            totalLines += value
            print(key + ": " + str(value))
    except IOError:
        print('{0} does not exist.'.format(dir))
    else:
        print('\nResult: {0} lines in {1} files'.format(str(totalLines), str(totalFiles)))