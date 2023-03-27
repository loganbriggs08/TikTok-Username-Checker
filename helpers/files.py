import os 

URL_Base: str = "https://www.tiktok.com"

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

def add_username(dir_name: str, file_name: str, username: str):
    with open(f"./{dir_name}/{file_name}.txt", 'a') as f:
        f.write(f"\n{URL_Base}/@{username}")
        f.close()