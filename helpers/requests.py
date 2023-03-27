import httpx

from colorama import * 

URL_Base: str = "https://www.tiktok.com"

def username_available(username: str) -> bool: 
    response = httpx.get(f"{URL_Base}/@{username}")
        
    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} Couldn't fetch username.")