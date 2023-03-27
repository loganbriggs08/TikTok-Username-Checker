import httpx 

URL_Base: str = "https://www.tiktok.com"

def username_available(username: str) -> bool: 
    response = httpx.get(f"{URL_Base}/@{username}")
    
    if response.status_code == 200:
        return False
    elif response.status_code == 404:
        return False
    else:
        return False