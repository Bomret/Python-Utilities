'''
Created on 27.09.2011

@author: stefan
'''
import os
import sys
from com.bomret.util.terminalutils import PicSorter

if __name__ == "__main__":
    sorter = PicSorter()
        
    print('Starting to sort...')
    if len(sys.argv) < 2:
        sorter.sort(os.getcwd())
    else:
        sorter.sort(sys.argv[1])
    print('Finished!')
