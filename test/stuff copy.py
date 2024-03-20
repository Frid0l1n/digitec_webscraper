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
            response.raise_for_status()  # Raise an exception for unsuccessful HTTP requests
            soup = BeautifulSoup(response.content, "html.parser")

            spans = soup.find_all("span", {"aria-label": lambda x: x and "CHF" in x})

            # Extract product name
            strong = soup.find_all("strong")
            product_name = strong[-1].text if strong else "Product Name not found"

            # Extract product description
            titles = soup.find_all("h1")
            product_description = (
                titles[0].text if titles else "Product Description not found"
            )

            print("Product:", product_name, "Description:", product_description)

            if spans:
                target_span = spans[0].text
                print("Price:", target_span)
            else:
                print("No price found for", url)

        except requests.exceptions.RequestException as e:
            print("Error fetching data for", url, ":", e)

    time.sleep(60)
