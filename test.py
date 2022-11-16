from datetime import datetime
from os import system
import serial
import time

# 0 establishing serial connection
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=3.0)
ser.reset_input_buffer()


def motors(command, seconds):
    ser.write(bytes(command, "utf-8"))
    time.sleep(seconds)


# 1 creating base folder
dtn = datetime.now()
base_folder = dtn.strftime("%m-%d-%H-%M")
cmd_mkdir_base = "mkdir /home/bentanay/" + base_folder
system(cmd_mkdir_base)

# 2 creating layer folders
layers = ["1", "2", "3", "4", "5"]
for x in layers:
    layer_folder = "L" + x
    cmd_mkdir_layer = "mkdir /home/bentanay/" + base_folder + "/" + layer_folder
    system(cmd_mkdir_layer)

# 3 copying pi repository to windows
cmd_scp = (
    'sshpass -p "duckybot2" scp -r /home/bentanay/'
    + base_folder
    + " benta@BLT:D:/PiRepo"
)
system(cmd_scp)

# 4 layer photos & storage
increments = ["1", "2", "3", "4", "5", "6", "7", "8"]
for i in layers:
    for j in increments:
        photo = "L" + i + "P" + j + ".jpg"
        layer_folder = "L" + i
        photo_path = "/home/bentanay/" + base_folder + "/" + layer_folder + "/" + photo
        cmd_libcamera = (
            "libcamera-jpeg -o " + photo_path + " -t 0001 --width 640 --height 480"
        )
        system(cmd_libcamera)
        motors("F", 2)
    motors("R", 10)
    motors("U", 5)
motors("D", 0)

# 5 copying updated pi repository to windows
system(cmd_scp)
