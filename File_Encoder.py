from DirectoryEncoderOrDecoder import Total_files, dir_decrypt, dir_encrypt, dir_search

def front_face_code():
    request = input("Decrypt or Encrypt or Search?: ")
    request=request.lower()

    if(request == "decrypt"):
        user_dir= input("Enter your file directory to Decrypt: ")
        try:
            dir_decrypt(user_dir)
            print(f"Total Files Decrypted = {len(Total_files)}")
        except:
            print("Something went wrong!")

    elif(request == 'encrypt'):
        user_dir = input("Enter your file directory to Encrypt: ")
        try:
            dir_encrypt(user_dir)
            print(f"Total Files Encrypted = {len(Total_files)}")
        except:
            print("Something went wrong")
    elif(request == 'search'):
        user_dir = input("Enter your file directory to Search: ")
        try:
            dir_search(user_dir)
            print(f"Total Files  = {len(Total_files)}")
        except:
            print("Something Went Wrong")
    else:
        print("\nPlease Enter valid request from | Encrypt | Decrypt | Search |")
        front_face_code()


if __name__ =="__main__":
    front_face_code()


 

 
 
 