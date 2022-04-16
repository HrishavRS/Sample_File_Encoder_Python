import os
from EncoderAndDecoder import convertor, revertor, convertor_test
import pickle

Total_files = []
Total_UnEncryptable_Files = []
def dir_search(location):
    change_dir = location
    os.chdir(change_dir)
    current_dir = os.listdir()
    location = []
    folders = []
    for item in current_dir:
        if (os.path.isdir(item)):
            location.append(item)
            Total_files.append(item)
            # new_name = convertor(folder_name)
            # os.rename(folder_name,new_name)
            folders.append(item)
        else:
            location.append(item)
            Total_files.append(item)
            # new_name = convertor(file_name)
            # os.rename(file_name,new_name)

    print(f"\nTotal Files in '{change_dir}' = {len(location)}")
    if(len(folders)!=0):
        print(f"\tFolder Present in '{change_dir}' = YES \n\tTotal Amount of Folder Present = {len(folders)}")
        for folder in folders:
            new_dir = change_dir + "/"+ folder
            dir_search(new_dir)
    else:
        print(f"\tFolder Present in '{change_dir}' = NO\n")      

def dir_encrypt_test(location):
    change_dir = location
    os.chdir(change_dir)
    current_dir = os.listdir()
    location = []
    folders = []
    unEncryptable_files = []
    for item in current_dir:
        if(os.path.isdir(item)):
            location.append(item)
            test,rename_overflow = convertor_test(item)
            Total_files.append(item)
            folders.append(item)
            if(test>0 or rename_overflow):
                unEncryptable_files.append(item)
                Total_UnEncryptable_Files.append(item)

        else:
            location.append(item)
            test,rename_overflow = convertor_test(item)
            Total_files.append(item)
            if(test>0 or rename_overflow):
                unEncryptable_files.append(item)
                Total_UnEncryptable_Files.append(item)

    print(f"\nTotal Files in {change_dir} = {len(location)}")
    if(len(unEncryptable_files)!=0):
        print(f"\tTotal UnEncryptable Files in '{change_dir}' = {len(unEncryptable_files)}")
        print(f"\tTotal UnEncryptable Files are =")
        for item in unEncryptable_files:
            print(f"\t{item}")
        print("\n")

    else:
        print(f"\tNo UnEncryptable Files in '{change_dir}'")
    
    if(len(folders)!=0):
        print(f"\tFolder Present in '{change_dir}' = YES \n\tTotal Amount of Folder Present = {len(folders)}")
        for folder in folders:
            new_dir = change_dir + "/"+ folder
            dir_encrypt_test(new_dir)
    else:
        print(f"\tFolder Present in '{change_dir}' = NO\n")
    
def dir_encrypt(location):
    change_dir = location
    os.chdir(change_dir)
    current_dir = os.listdir()
    location = []
    folders = []
    for item in current_dir:
        if(os.path.isdir(item)):
            location.append(item)
            new_name = convertor(item)
            Total_files.append(new_name)
            folders.append(new_name)
            os.rename(item,new_name)

        else:
            location.append(item)
            Total_files.append(item)
            new_name = convertor(item)
            os.rename(item,new_name)

    print(f"\nTotal Files in '{change_dir}' = {len(location)}")
    if(len(folders)!=0):
        print(f"\tFolder Present in '{change_dir}' = YES \n\tTotal Amount of Folder Present = {len(folders)}")
        for folder in folders:
            new_dir = change_dir + "/"+ folder
            dir_encrypt(new_dir)
    else:
        print(f"\tFolder Present in '{change_dir}' = NO\n")
     
def dir_decrypt(location):
    change_dir = location
    os.chdir(change_dir)
    current_dir = os.listdir()
    location = []
    folders = []
    for item in current_dir:
        encoded_name = item
        original_name = revertor(item)
        os.rename(encoded_name,original_name)
        Total_files.append(item)

    updated_current_dir = os.listdir()
    for item in updated_current_dir:
        if(os.path.isdir(item)):
            folders.append(item)
    if(len(folders)!=0):
        print(f"Folder Present in '{change_dir}' = YES \n\tTotal Amount of Folder Present = {len(folders)}")
        for folder in folders:
            print(folder)
            new_dir = change_dir + "/"+folder
            dir_decrypt(new_dir)
    else:
        print(f"\tFolder Present in '{change_dir}' = NO\n")

# dir_search(user_dir)
# dir_encoder(user_dir)
# dir_decoder(user_dir)
# pickle_in = open("All File Names Here.pickle","wb")
# pickle.dump(Total_files,pickle_in)