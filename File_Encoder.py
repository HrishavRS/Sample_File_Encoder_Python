from DirectoryEncoderOrDecoder import Total_files, dir_search,dir_decoder,dir_encoder

def front_face_code():
    request = input("Decode or Encode or Search?: ")
    request=request.lower()

    if(request == "decode"):
        user_dir= input("Enter your file directory to Decode: ")
        try:
            dir_decoder(user_dir)
            print(f"Total Files Decoded = {len(Total_files)}")
        except:
            print("Something went wrong!")

    elif(request == 'encode'):
        user_dir = input("Enter your file directory to Encode: ")
        try:
            dir_encoder(user_dir)
            print(f"Total Files Encoded = {len(Total_files)}")
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
        print("\nPlease Enter valid request from | Encode | Decode | Search |")
        front_face_code()

front_face_code()


 

 
 
 