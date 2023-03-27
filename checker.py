from helpers.files import create_dir, create_file

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
        
        
if __name__ == "__main__":
    Checker.setup()