import requests
from bs4 import BeautifulSoup
import webbrowser

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

q = input("Search on : ")

if q == "g":
    a = input("Google search : ")
    webbrowser.open("https://www.google.com/search?q="+a +
                    "&oq=ig&aqs=chrome..69i57j0l7.1351j0j8&sourceid=chrome&ie=UTF-8")
elif q == "yt":
    a = input("Youtube Search : ")
    webbrowser.open("https://www.youtube.com/results?search_query="+a)

elif q == "an":
    an = input("Anime Search : ")

    URL = "https://myanimelist.net/anime.php?q="+an

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    x = soup.find("a", {"class": "hoverinfo_trigger fw-b fl-l"}).get_text()
    if a.lower() == x.lower():
        webbrowser.open(
            soup.find('a', {'class': 'hoverinfo_trigger fw-b fl-l'})['href'])
    else:
        webbrowser.open(URL)
