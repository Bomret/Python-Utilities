'''
Created on 27.09.2011

@author: Stefan Reichel <dev@bomret.com>
'''

import os
from fnmatch import fnmatch
from logging import warning, info
from shutil import move
from PIL import Image
from PIL.ExifTags import TAGS
from mimetypes import guess_type
import re

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

class FileLister(object):
    '''
    
    '''
    
    def find_files(self, txtname, directory, extension):
        '''
        Function to find files in the specified directory with the specified
        extension. These will be written to a file with the specified name (txtname)
        in the current working directory, one filename per line.
        '''
    
        files = os.listdir(directory)
        extfiles = [file for file in files if fnmatch(file, '*.' + extension)]

        handle = open(txtname, 'w')

        for file in extfiles:
            handle.write(file + '\n')
            handle.close()
            
class PicSorter(object):
    '''
    This class sorts images in a given dir and its subdirs. At the moment it
    sorts jpeg images in folders after the contained creation date.
    The structure is year / month / day / filename.
    If the date could not be determined or is not included the image is
    stored in the folder "undated".
    '''
    
    def sort(self, topdir):
        '''
        This method does the actual sorting. It takes the top working dir
        as parameter and sorts the images within it and its subfolders.
        '''
        
        pics = self.__getAllPicsWithPath(topdir)
        
        for pic in pics:
            path = 'undated'
            date = self.__getDate(pic)
                        
            if date:
                year = date[0]
                month = date[1]
                day = date[2]
                           
                path = topdir + '/' + year + '/' + month + '/' + day
            else:
                warning(str(pic) + ' contains no EXIF or date information. Will be saved in undated.')
            
            if not os.path.exists(path):
                os.makedirs(path)
          
            try:
                move(pic, path)
            except:
                pass

        self.__removeEmptyDirs(topdir)
        
    def __getDate(self, filename):
        '''
        '''
        image = open(filename)
        exif = image._getexif()
        
        if not exif:
            return None
        
        for tag, value in exif.items():
            decoded = TAGS.get(tag, tag)
            if decoded == 'DateTime':
                if value != '':
                    date = value.split(' ')[0].split(':')
                
        if date:
            return date
        else:
            return None
        
    def __getAllPicsWithPath(self, topDir):
        '''
        '''
        picList = []
        for root, dirnames, filenames in os.walk(topDir):
            for filename in filenames:
                mime = guess_type(filename)
            
                if 'image/jpeg' in mime:
                    picList.append(os.path.join(root, filename))
                
        return picList

    def __removeEmptyDirs(self, topDir):
        '''
        '''
        for root, dirs, in os.walk(topDir, topdown=False):
            for subdir in dirs:
                try:
                    os.rmdir(os.path.join(root, subdir))
                except:
                    pass
                
class ImageConverter(object):
    '''
    This class is used to convert all images within a given folder to a new
    format specified by the extension.
    '''
    
    def convert(self, workdir, newextension):
        '''
        This method does the actual conversion. It takes the workdir and
        the extension of the desired format as parameters. If the conversion
        process fails an IOError is raised.
        '''
        for infile in os.listdir(workdir):
            filename, extension = os.path.splitext(infile)
            outfile = filename + "." + newextension
            mime = guess_type(infile)
            
            if infile != outfile and 'image' in mime:
                try:
                    info("Trying to convert ", infile)
                    Image.open(infile).save(outfile)
                except IOError:
                    warning("Cannot convert ", infile)

class TextIndexer(object):
    
    def __init__(self):
        self.__worddict = dict()
        
    def index_dir(self, workdir):
        textfiles = [file for file in workdir if fnmatch(file, "*.txt")]
        
        for file in textfiles:
            path = os.path.join(workdir, file)
            tempfile = open(path, 'r')
            content = tempfile.read()
            words = re.split('[\s,.;!\?()\[\]\{\}]', content)
            
            for word in words:
                if word not in self.__worddict:
                    self.__worddict[word] = [file]
                elif file not in self.__worddict[word]:
                    self.__worddict[word].append(file)
                
                del self.__worddict['']
        
        return self.__worddict