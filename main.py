import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://laravel-quiz-app.onrender.com/quizzes/create"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").text
    print(f"ページタイトル: {title}")

if __name__ == "__main__":
    scrape()
