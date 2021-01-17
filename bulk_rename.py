import os
path = os.chdir("/home/vijesh/Downloads/test")
i = 0
for file in os.listdir(path):
    new_file_name = "pic{}.jpg".format(i)
    os.rename(file, new_file_name)
    i = i+1
