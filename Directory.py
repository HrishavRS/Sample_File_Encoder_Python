import os
from EncoderAndDecoder import convertor, revertor
import pickle

Total_files = []
def dir_search(location):
    change_dir = location
    os.chdir(change_dir)
    current_dir = os.listdir()
    location = []
    folders = []
    for item in current_dir:
        item = item.split(".")
        if (len(item)>1):
            file_name = item[0]+"."+item[1]
            location.append(file_name)
            Total_files.append(file_name)
            # new_name = convertor(file_name)
            # os.rename(file_name,new_name)
        else:
            folder_name = item[0]
            location.append(folder_name)
            Total_files.append(folder_name)
            # new_name = convertor(folder_name)
            # os.rename(folder_name,new_name)
            folders.append(folder_name)

    print(f"\nTotal Files in {change_dir} = {len(location)}")
    if(len(folders)!=0):
        print(f"Folder Present in {change_dir} = YES \nTotal Amount of Folder Present = {len(folders)}")
        for folder in folders:
            new_dir = change_dir + "/"+ folder
            dir_search(new_dir)
    else:
        print(f"Folder Present in {change_dir} = NO\n")      

    
def dir_encoder(location):
    change_dir = location
    os.chdir(change_dir)
    current_dir = os.listdir()
    location = []
    folders = []
    for item in current_dir:
        item = item.split(".")
        if(len(item)>1):
            file_name = item[0]+"."+item[1]
            location.append(file_name)
            Total_files.append(file_name)
            new_name = convertor(file_name)
            os.rename(file_name,new_name)
        else:
            folder_name = item[0]
            location.append(folder_name)
            new_name = convertor(folder_name)
            Total_files.append(new_name)
            folders.append(new_name)
            os.rename(folder_name,new_name)

    print(f"\nTotal Files in {change_dir} = {len(location)}")
    if(len(folders)!=0):
        print(f"Folder Present in {change_dir} = YES \nTotal Amount of Folder Present = {len(folders)}")
        for folder in folders:
            new_dir = change_dir + "/"+ folder
            dir_encoder(new_dir)
    else:
        print(f"Folder Present in {change_dir} = NO\n")
     
def dir_decoder(location):
    change_dir = location
    os.chdir(change_dir)
    current_dir = os.listdir()
    location = []
    folders = []
    for item in current_dir:
        encoded_name = item
        original_name = revertor(item)
        os.rename(encoded_name,original_name)
    updated_current_dir = os.listdir()
    for item in updated_current_dir:
        item = item.split(".")
        if(len(item) == 1):
            folders.append(item[0])
    if(len(folders)!=0):
        print(f"Folder Present in {change_dir} = YES \nTotal Amount of Folder Present = {len(folders)}")
        for folder in folders:
            print(folder)
            new_dir = change_dir + "/"+folder
            dir_decoder(new_dir)
    else:
        print(f"Folder Present in {change_dir} = NO\n")



# dir_search(user_dir)
# dir_encoder(user_dir)
# dir_decoder(user_dir)
# pickle_in = open("All File Names Here.pickle","wb")
# pickle.dump(Total_files,pickle_in)