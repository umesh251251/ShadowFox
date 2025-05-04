import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.shadowfox.in/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"
}

try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status() 

    soup = BeautifulSoup(response.content, "html.parser")
    print("\nSuccessfully fetched and parsed the page!")
    print(f"\nPage Title: {soup.title.string.strip() if soup.title else 'No Title Found'}")

    print("\n All <h1> Tags:")
    for i, heading in enumerate(soup.find_all("h1"), start=1):
        print(f"{i}. {heading.text.strip()}")

    print("\nAll Links (Text and URL):")
    links = []
    for link in soup.find_all("a", href=True):
        text = link.text.strip()
        href = link["href"]
        if href:
            print(f"- {text if text else '[No Text]'} -> {href}")
            links.append([text, href])

    with open("webscrapper.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Link Text", "URL"])
        writer.writerows(links)
    print("\nLinks saved to 'webscrapper.csv'.")

except requests.exceptions.RequestException as e:
    print("\nError fetching the page:", e)
except Exception as e:
    print("\nGeneral error:", e)
