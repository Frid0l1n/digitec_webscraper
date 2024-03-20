import requests
from bs4 import BeautifulSoup
import datetime
import time
import pandas as pd
import os

# Initialize list of URLs
urls = []

with open("urls.txt", "r") as f:
    for line in f:
        urls.append(line.strip())

if os.path.isfile("table.csv"):
    df = pd.read_csv("table.csv")
    print(df)
else:
    df = {
        "Time": [],
        "Product": [],
        "Price": [],
    }

    df = pd.DataFrame(df)
    df.to_csv("table.csv", index=False)
    print(df)

time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
                target_span = target_span.text.strip()
                print("Product:", product_description, "Price:", target_span)

                new_data = {
                    "Time": [time_now],
                    "Product": [product_description],
                    "Price": [target_span],
                }

                new_df = pd.DataFrame(new_data)
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_csv("table.csv", index=False)

            else:
                print("No price found for", url)

        except requests.exceptions.RequestException as e:
            print("Error fetcghing data for:", url, ":", e)

    time.sleep(60 * 10)
