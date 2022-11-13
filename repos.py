from datetime import datetime

# 1 creating base folder
print('# 1. creating base folder')
dtn = datetime.now()
base_folder = dtn.strftime('%m-%d-%H-%M')
cmd = 'mkdir /home/bentanay/' + base_folder
print(cmd)

# 2 creating layer folders
print('# 2. creating layer folders')
for x in range(5):
    x_inc = x + 1
    layer_folder = 'L' + str(x_inc)
    cmd = 'mkdir /home/bentanay/' + base_folder + '/' + layer_folder
    print(cmd)

# 3 copying pi repository to windows
print("# 3. copying pi repository to windows")
print("scp ...")

# 4 layer photos & storage
print('# 4a. layer photos & storage')
for x in range(5):
    L = x + 1
    for y in range(12):
        P = y + 1
        photo = 'L' + str(L) + 'P' + str(P) + '.jpg'
        layer_folder = 'L' + str(L)
        print('save ' + photo + ' to /home/bentanay/' + base_folder + '/' + layer_folder)
        # F
    print('# 4b. copying layer ' + str(L) + ' to windows')
    # R
    # U
    print('scp ...')
    print('prompt to continue')
# D