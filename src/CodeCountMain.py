'''
Created on 27.09.2011

@author: Stefan Reichel <dev@bomret.com>
'''
import argparse
from com.bomret.util.terminalutils import CodeCounter
import os

if __name__ == '__main__':
    dir = os.getcwd()
    extensions = ['c', 'h', 'cpp', 'hpp', 'java', 'php', 'py', 'as', 'mxml', 'js']
    
    counter = CodeCounter()
    parser = argparse.ArgumentParser(description="Count lines of code in all source code files in a dir and its subdirs.")

    try:
        countedFiles = counter.count_code(dir, extensions)
        totalFiles = len(countedFiles)
        totalLines = 0

        for key, value in countedFiles.iteritems():
            totalLines += value
            print(key, value)
    except IOError:
        print('Could not open ' + str(dir))
    else:
        print(str(totalLines) + " lines in " + str(totalFiles) + " files.")