from colorama import *
from helpers.requests import username_available
from helpers.files import create_dir, create_file, add_username

init(convert=True)

class Checker: 
    def __init__(self) -> None:
        pass
    
    def setup() -> bool:
        if create_dir("data") == True:
            create_file("data", "available")
            create_file("data", "unavailable")
            return True 
        else:
            return False
        
    def check_username(username: str) -> bool: 
        try:
            response = username_available(username)
            return response
        except:
            return False
        
    def add_username(dir_name: str, file_name: str, username: str): 
        add_username(dir_name, file_name, username)
        
if __name__ == "__main__":
    Checker.setup()
    
    try:
        with open("usernames.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                raise Exception(f"{Fore.RED}[ERROR]{Fore.RESET} File is empty, please add some usernames.")
            else:
                for line in lines:
                    if line.strip():
                        result = Checker.check_username(line.strip())
                        
                        if result == True:
                            print(f"{Fore.GREEN} https://www.tiktok.com/@{line.strip()}")
                            Checker.add_username("./data", "available", line.strip())
                            
                        elif result == False:
                            print(f"{Fore.RED} https://www.tiktok.com/@{line.strip()}")
                            Checker.add_username("./data", "unavailable", line.strip())
                            
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} Please create a usernames.txt file.")