import os 

def create_dir(directory_name: str) -> bool: 
    if os.path.exists(f"./{directory_name}"):
        return False
    else:
        try:
            os.mkdir(f"./{directory_name}")
            return True
        except:
            return False
        
def create_file(dir_name: str, file_name: str) -> bool: 
    if os.path.exists(f"./{dir_name}"):
        with open(f"./{dir_name}/{file_name}.txt", 'w') as f:
            f.close()
            return True
    else:
        return False
    