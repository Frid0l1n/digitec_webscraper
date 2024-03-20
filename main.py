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
        try:

            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            spans = soup.find_all("span")
            titles = soup.find_all("h1")
            strong = soup.find_all("strong")
            span = soup.find_all("span")
            # find product type
            if titles:
                product_description = titles[0].text
            else:
                print("Product not found")

            target_span = None
            # Search for the <span> with "CHF" in aria-label attribute
            for span in spans:
                aria_label = span.get("aria-label")
                if aria_label and "CHF" in aria_label:
                    target_span = span
                    break

            if target_span:
                target_span = target_span.text
                print(
                    "Product: ",
                    product_description,
                    "Price: ",
                    target_span,
                )
            else:
                print("No price found for", url)

        except requests.exceptions.RequestException as e:
            print("Error fetcghing data for:", url, ":", e)

    time.sleep(60)
