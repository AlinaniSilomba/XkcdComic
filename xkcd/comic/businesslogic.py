import requests

#This is out business logic for getting the data from xkcd.com


def GetCurrentComic()->dict['str':'str']:
    baseUrl = f"https://xkcd.com/info.0.json"
    response = requests.get(baseUrl)
    response.raise_for_status()
    data = response.json()
    return data

'''
*TODO find a way to hold state of the number of the comic 
"https://xkcd.com/Next 
"https://xkcd.com/previous 
works in the Url the buttons are yet to be wired up 

'''
def get_comic_number()->int:
    baseUrl = f"https://xkcd.com/info.0.json"
    response = requests.get(baseUrl)
    response.raise_for_status()
    data:dict['str':'strt'] = response.json()
    num:int= int(data['num'])
    return num


def GetNextComic() -> dict['str':'str']:
    num:int = get_comic_number()
    comicNumber:int = num
    if comicNumber == num:
         issue:int = comicNumber +  1
         baseUrl = f"https://xkcd.com/{issue}/info.0.json"
         response = requests.get(baseUrl)
         response.raise_for_status()
         data = response.json()
         return data

def GetPreviousComic()->dict['str':'str']:
    num = get_comic_number()
    comicNumber = num
    if comicNumber == num:
         issue:int = comicNumber - 1
         baseUrl = f"https://xkcd.com/{issue}/info.0.json"
         response = requests.get(baseUrl)
         response.raise_for_status()
         data = response.json()
         return data

'''
 To be implemented later
def GetRandomComic(comicNumber):
    baseUrl = f"https://xkcd.com/{comicNumber}/info.0.json"
    response = requests.get(baseUrl)
    response.raise_for_status() 
    data = response.json()
    return data
'''