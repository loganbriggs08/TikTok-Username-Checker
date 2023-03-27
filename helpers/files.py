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
    