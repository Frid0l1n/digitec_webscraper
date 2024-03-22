import requests
from bs4 import BeautifulSoup
import datetime
import time
import os
import json
import validators
import csv

# Initialize list of URLs
urls = []


# TODO Add a way to add and remove links
while True:
    link = input("Enter link (or type 'q' to quit): ")

    if link.lower() == "q":
        break

    if validators.url(link):
        urls.append(link)
    else:
        print("Invalid URL. Please try again.")

# print("Links added to the JSON file.")

# TODO auto create json file

# Read JSON data
with open("urls.json", "r") as f:
    data = json.load(f)
    if data["urls"]:
        urls.extend(data["urls"])
    else:
        print("No URLs found in the JSON file.")


with open("urls.json", "w") as f:
    json.dump({"urls": urls}, f, indent=2)

data = {
    "ID": [],
    "Time": [],
    "Product": [],
    "Price": [],
    "Change": [],
}

if os.path.isfile("table.csv"):
    reader = csv.reader(open("table.csv"))
    next(reader, None)
    for row in reader:
        data["ID"].append(row[0])
        data["Time"].append(row[1])
        data["Product"].append(row[2])
        data["Price"].append(row[3])
        data["Change"].append(row[4])

# Continuously fetch prices for all URLs
while True:
    for url in urls:
        try:
            # id
            id = url.split("-")[-1]

            # time
            time_now = datetime.datetime.now()

            response = requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                },
            )
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
                # TODO: Fix isnumeric
                target_span = int("".join(filter(str.isnumeric, target_span.text)))
                old_price = (
                    float(data["Price"][::-1][data["ID"][::-1].index(id)])
                    if id in data["ID"]
                    else float(target_span)
                )
                change = float(target_span) - old_price

                data["ID"].append(id)
                data["Time"].append(str(time_now))
                data["Product"].append(product_description)
                data["Price"].append(str(target_span))
                data["Change"].append(str(change))

                rows = []

                for i in range(len(data["ID"])):
                    rows.append(
                        [
                            data["ID"][i],
                            data["Time"][i],
                            data["Product"][i],
                            data["Price"][i],
                            data["Change"][i],
                        ]
                    )

                with open("table.csv", "w") as f:
                    # Write header
                    f.write(f"{','.join(data.keys())}\n")

                    # Write rows
                    for row in rows:
                        f.write(f"{','.join(row)}\n")

            # TODO: Async task requests
            else:
                print("No price found for", url)

        except requests.exceptions.RequestException as e:
            print("Error fetching data for:", url, ":", e)

        except (Exception, KeyboardInterrupt) as e:
            raise e

    time.sleep(3)
