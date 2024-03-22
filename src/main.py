import requests
from bs4 import BeautifulSoup
import datetime
import time
import pandas as pd
import os
import json
import validators

# Initialize list of URLs
urls = []

while True:
    link = input("Enter link (or type 'q' to quit): ")

    if link.lower() == "q":
        break

    if validators.url(link):
        urls.append(link)
    else:
        print("Invalid URL. Please try again.")

with open("urls.json", "w") as f:
    json.dump({"urls": urls}, f)

print("Links added to the JSON file.")

# Read JSON data
with open("urls.json", "r") as f:
    data = json.load(f)
    if "urls" in data:
        urls = data["urls"]
    else:
        print("No URLs found in the JSON file.")

if os.path.isfile("table.csv"):
    df = pd.read_csv("table.csv")
else:
    df = {
        "ID": [],
        "Time": [],
        "Product": [],
        "Price": [],
    }

    df = pd.DataFrame(df)
    df.astype({"Time": "string", "Product": "string", "Price": "int"})
    df.to_csv("table.csv", index=False)


time_now = datetime.datetime.now()


# Continuously fetch prices for all URLs
while True:
    for url in urls:
        try:

            id = url.split("-")[-1]
            print(id)

            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            spans = soup.find_all("span")
            titles = soup.find_all("h1")
            strong = soup.find_all("strong")
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
                # TODO: Fix this
                target_span = int("".join(filter(str.isdigit, target_span.text)))
                print("Product:", product_description, "Price:", target_span)

                new_data = {
                    "ID": [id],
                    "Time": [time_now],
                    "Product": [product_description],
                    "Price": [target_span],
                }

                new_df = pd.DataFrame(new_data)
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_csv("table.csv", index=False)

                for i in range(len(new_data["Price"])):
                    difference = new_data["Price"][i] - new_data["Price"][i - 1]
                    print(difference)
            else:
                print("No price found for", url)

        except requests.exceptions.RequestException as e:
            print("Error fetcghing data for:", url, ":", e)

        except (Exception, KeyboardInterrupt) as e:
            print(e)

    time.sleep(10)
