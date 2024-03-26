import json

with open("test.json") as f:
    data = json.load(f)


def remove_link(url_to_remove):
    if url_to_remove in data["urls"]:
        data["urls"].remove(url_to_remove)


remove_link(
    "https://www.digitec.ch/de/s1/product/samsung-flip-4-pro-wm65b-3840-x-2160-pixel-65-digital-signage-21670692"
)

print(json.dumps(data, indent=2))
