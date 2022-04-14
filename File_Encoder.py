from DirectoryEncoderOrDecoder import Total_files, Total_UnEncryptable_Files, dir_decrypt, dir_encrypt, dir_search,dir_encrypt_test

def front_face_code():
    request = input("Decrypt or Encrypt or Search?: ")
    request=request.lower()

    if(request == "decrypt" or request == 'd'):
        user_dir= input("Enter your file directory to Decrypt: ")
        try:
            dir_decrypt(user_dir)
            print(f"Total Files Decrypted = {len(Total_files)}")


        except:
            print("Something went wrong!")

    elif(request == 'encrypt' or request == 'e'):
        test_request = input("Do you want to 'Check For Success' before executing Encryption? (Y/N): ")
        test_request = test_request.lower()
        try:
            if(test_request =='n'):
                warning = input("Warning: Encryption is being executed without test. Enter 'Y' to continue or 'N' to go back: ")
                if(warning.lower()=='y'):
                    user_dir = input("Enter your directory to Encrypt: ")
                    dir_encrypt(user_dir)
                    print(f"Total Files Encrypted = {len(Total_files)}")
                if(warning.lower()=='n'):
                    front_face_code()
            else:
                user_dir = input("Enter your directory to Encrypt to 'Check For Success': ")
                dir_encrypt_test(user_dir)
                print(f"Total Files ={len(Total_files)}")
                print(f"Total UnEncryptable Files = {len(Total_UnEncryptable_Files)}")
                if(len(Total_UnEncryptable_Files)>0):
                    print("\n\t\t\tXXXXX UNSAFE TO PERFORM ENCRYPTION HERE XXXX\n")
                else:
                    print("\n\t\t\t🗸🗸🗸🗸 SAFE TO PERFORM ENCRYPTION 🗸🗸🗸🗸🗸\n")
        except:
            print("Something went wrong")
    elif(request == 'search' or request == 's'):
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


 

 
 
 