import requests
from fastapi import FastAPI
BASEURL = "http://time.com"
app = FastAPI()
from bs4 import BeautifulSoup

@app.get("/getTimeStories")
def root():
    response = requests.get(BASEURL)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    featured_voices = soup.find("ul", {"class":"featured-voices__list"})
    all_objs = []
    for li in featured_voices.find_all("li"):
        a_all = li.find_all("a")
        link = a_all[1]['href']
        title = li.find("h3").string
        obj = {
            "title":title,
            "link":BASEURL+link
        }
        all_objs.append(obj)
    return all_objs


