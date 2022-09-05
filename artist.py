import requests
from bs4 import BeautifulSoup
import pandas as pd
artist = []
def getArtists(lettre, page):
    
    url = f'https://www.artsy.net/artists/artists-starting-with-{lettre}?page={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    nom=soup.find_all("a",{"class":"RouterLink__RouterAwareLink-sc-1nwbtp5-0 ArtistsByLetter__Name-sc-1f86lqh-1 dPqrct"})
    for i in range (len(nom)):
        artist.append(nom[i].text) 
    
    
    print(artist)    
def listAlphabet():
    return [chr(i) for i in range(ord('a'),ord('z')+1)]
    
      

for x in listAlphabet():
    
    for y in range(0,15):
        getArtists(x,y)
        
           

df=pd.DataFrame(artist)
df.to_excel('artists.xlsx',index=False)
print('Fin.')
