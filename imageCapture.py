import time
from os import system
from datetime import datetime

# log/files formatting
dtn = datetime.now()
fileName = dtn.strftime('%m-%d-%H-%M')
log = 'log.txt'
folderName = '/home/bentanay/' + fileName
fileInFolder = folderName + '/' + log
cmd = 'mkdir ' + folderName
system(cmd)

for x in range(2):
    for y in range(2):

        # r/c formatting
        with open(fileInFolder, 'a') as f:
            f.write('----------------------\n')
        row = 'r' + str(x)
        col = 'c' + str(y)
        index = row + col
        imageName = index + '.jpg'
        image = folderName + '/' + imageName

        # start timer
        s1 = time.time()

        # snap picture
        with open(fileInFolder, 'a') as f:
            f.write('1. Capturing image ' + imageName + '.\n')
        cmd = 'libcamera-jpeg -o ' + image \
            + ' -t 0001 --width 640 --height 480'
        system(cmd)
        with open(fileInFolder, 'a') as f:
            f.write('-- Image captured.\n')

        # timing report
        s2 = time.time()
        td = s2 - s1
        rtime = round(td, 2)
        srtime = str(rtime)
        with open(fileInFolder, 'a') as f:
            f.write('-- Capture of ' + imageName + ' took ' + srtime
                    + 's.\n')
