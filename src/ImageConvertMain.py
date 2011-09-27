'''
Created on 27.09.2011

@author: stefan
'''
from com.bomret.util.terminalutils import ImageConverter
import sys
import os

if __name__ == '__main__':
    converter = ImageConverter()
    if len(sys.argv) > 3:
        workdir = sys.argv[1]
        newextension = sys.argv[2]
    else:
        workdir = os.getcwd()
        newextension = "png"
    
    print("Starting conversion...")
    converter.convert(workdir, newextension)