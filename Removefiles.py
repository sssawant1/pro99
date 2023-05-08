import time
import shutil
import os

days = 30
path = "C:/Users/srish/Desktop/Byjus/pro99/file.txt"
def main():
    seconds = time.time()-(days*24*60*60)
    if(os.path.exists(path)):
        for root_folder,folder,files in os.walk(path):
            if(seconds>= getFileOrFolderTime(root_folder)):
                removeFolder(root_folder)
    else:
        print("not found")



def getFileOrFolderTime(path):
    createTime = os.stat(path).st_ctime
    return createTime

def removeFolder(path):
    os.remove(path)