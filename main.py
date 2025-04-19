import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.google.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").text
    print(f"ページタイトル: {title}")

if __name__ == "__main__":
    scrape()
