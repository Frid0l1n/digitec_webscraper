import requests
from bs4 import BeautifulSoup
import time

# Initialize list of URLs
urls = []

while True:
    link = input("Enter link (or type 'exit' to quit): ")
    if link.lower() == "exit":
        break

    urls.append(link)

# Continuously fetch prices for all URLs
while True:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        spans = soup.find_all("span")

        target_span = None
        # Search for the <span> with "CHF" in aria-label attribute
        for span in spans:
            aria_label = span.get("aria-label")
            if aria_label and "CHF" in aria_label:
                target_span = span
                break

        if target_span:
            print(target_span.text)
        else:
            print("No price found for", url)

    time.sleep(60)
