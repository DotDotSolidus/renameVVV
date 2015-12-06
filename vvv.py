import os
import sys

def filelist(path):
    for e in os.listdir(path):
        fullpath = os.path.join(path,e)
        if os.path.isdir(fullpath):
            filelist(fullpath)
        elif os.path.isfile(fullpath):
            file_name, ext = os.path.splitext(os.path.basename(fullpath))
            os.rename(fullpath,path+"%s.vvv" %(file_name)) 

if len(sys.argv) != 2:
    print("Usage: python vvv.py [path]")
    quit()

filelist(sys.argv[1])
