'''
Created on 27.09.2011

@author: Stefan Reichel <dev@bomret.com>
'''

import os
from fnmatch import fnmatch

class CodeCounter(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._files = dict()
    
    def count_code(self, workdir, extensions):
        '''
        
        '''
        if not os.path.exists(workdir):
            raise IOError
        
        for root, dirs, filenames in os.walk(workdir):
            for file in filenames:
                path = os.path.join(root, file)
                
                for ext in extensions:
                    if fnmatch(file, '*.' + ext):
                        handle = open(path, 'r')
                        length = len(handle.readlines())
                        self._files[str(file)] = length
                        handle.close()
                        
        return self._files