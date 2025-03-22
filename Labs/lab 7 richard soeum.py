import os
import hashlib

def menu():
    while True:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice =="1":
            directory =input("enter the directory path:")
            find_duplicates(directory)
        elif choice=="2":
            print("exiting program")
            break

    else: 
        print("invalid choice")


def find_duplicates(directory):
    if not os.path.isdir(directory):
        print(f" the directory {directory} does not exist.")
        return
    
    checksums={}


    # search os.walk(directory):
    for root,_, files in os.walk(directory):
        for file in files:
            file_path =os.path.join(root,file)
            file_hash=get_checksum

            if file_hash in checksums:
                checksums[file_hash].append(file_path)

            else:
                checksums[file_hash]=[file_path]

    duplicates_found=False
    for file_hash, file_paths in checksums.items():
        if len(file_paths)>1:
            duplicates_found=True
            print(f"\n duplicate files with hash {file_hash}:")
            for path in file_paths:
                print(path)

    if not duplicates_found:
        print("no dupes files found")
    

    # use a dictionary to store file names and paths
    # compare files with the same name

def get_checksum(file_path):

    hash_obj = hashlib.md5()  # Change to hashlib.sha256() if desired
    with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
    return hash_obj.hexdigest()
    
        


if __name__ == "__main__":
    menu()