import sys
from hash import FileHasher 
from jobs import  create_job_file
from exif import get_date
import os
from os.path import join, abspath 
 
def main(argv):
    src = argv[0]
    dest = argv[1]
    new_files_dict = get_new_files_dict(src, dest)
    create_job_file(src,dest,new_files_dict)
        
def get_new_files_dict(src, dest):
    dest_dict = get_hash_dict(dest)
    src_dict = get_hash_dict(src,dest_dict)
    return src_dict

def get_hash_dict(root,dest_dict=None):
    FH = FileHasher()
    hash_dict = dict()
    for file_path in get_files(root):                
        try:                            
            date , hashv = get_date(file_path) , FH.hash(file_path)
            if dest_dict == None :
                hash_dict[hashv] = [file_path , date]
            else:
                if hashv in dest_dict:
                    pass
                else:
                    hash_dict[hashv] = [file_path,date]                                     
        except:
            pass     
    return hash_dict

    
def get_files(root):
    for dirName, subdirList, fileList in os.walk(root):        
        for fname in fileList:
            path = abspath(join(dirName, fname))
            yield path    
    
if __name__ == "__main__":
    main(sys.argv[1:])    
