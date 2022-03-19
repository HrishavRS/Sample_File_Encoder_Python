from genericpath import isdir
import os

user_dir = input("Enter Your Directory: ")
# os.chdir(user_dir)
# print(os.listdir())
# for i in os.listdir():
#     i = i.split(".")
#     if(len(i)>1):
#         print("This is file=" + i[0])
#     else:
#         print("This is folder=" + i[0])    

# def directory_search(user_dir):
#     try:
#         os.chdir(user_dir)
#         files = os.listdir()
#         all_files = []
#         all_folders = []
#         for file in files:
#             file = file.split(".")
#             if(len(file) >1):
#                 all_files.append(file[0]+"."+files[1])
#             else:
#                 all_folders.append(file[0])
#         if(len(all_folders) != 0):
#             for i in all_folders:
#                 new_dir = user_dir+"/"+i


#     except:
#         print("Invalid Directory")

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
            location.append(item[0]+"."+item[1])
            Total_files.append(item[0]+"."+item[1])
        else:
            location.append(item[0])
            folders.append(item[0])
            Total_files.append(item[0])
    print(f"Total Files in {change_dir} = {len(location)}")
    if(len(folders)!=0):
        print(f"Folder Present in {change_dir} = YES \nTotal Amount of Folder Present = {len(folders)}")
        for folder in folders:
            new_dir = change_dir + "/"+ folder
            dir_search(new_dir)
    else:
        print(f"Folder Present in {change_dir} = NO\n")        

dir_search(user_dir)
print(f"Total Files in the Directory = {len(Total_files)}")