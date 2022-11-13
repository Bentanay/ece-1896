from datetime import datetime
# Online Python - IDE, Editor, Compiler, Interpreter

# 1  creating base folder
print('--- 1. creating base folder ---');
dtn = datetime.now();
base_folder = dtn.strftime('%m-%d-%H-%M');
cmd = 'mkdir /home/bentanay/' + base_folder;
print('creating base folder:\t\t' + cmd);

# 2  creating layer folders
print('--- 2. creating layer folders ---')
for x in range(5):
    x_inc = x + 1;
    layer_folder = 'layer-' + str(x_inc);
    cmd = 'mkdir /home/bentanay/' + base_folder + '/' + layer_folder;
    print('creating layer folder ' + str(x_inc) + ':\t' + cmd);

# 3     copying pi file directory to windows
print("--- 3. copying pi file director to windows ---")
print("copying pi file director to windows")

# 4
print('--- 4. taking/storing photos, copying files to windows')
for x in range(5):
    L = x + 1;
    for y in range(12):
        P = y + 1;
        photo = 'L' + str(L) + 'P' + str(P) + '.jpg';
        print('taking and storing photo ' + photo + ':\t');
    print('--- copying layer ' + str(L) + ' to windows')