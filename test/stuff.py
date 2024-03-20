import requests

cookies = {}

headers = {
    "authority": "www.digitec.ch",
    "accept": "*/*",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    # 'cookie': '.xpid=b03917f8; .cid=15425601-1a0e-497a-92d0-2f39045f3d90; .bid=2a83eea5-e570-4e48-9ffd-9c82f1ee7640; sp=02b50477-495b-480f-9f60-9e1938305487; RedirectCountry=off; _abck=BDA00F30E3999CCD39E661B682039073~-1~YAAQFFJDUCHoNxuLAQAAYD7FOAqAzDV9Ik+gtQYeVM2CwiwIAxLVXSSILlMYwuO8DOU+3oi8Gb3ILcNZqWNokk4bRtpMQRF6JT5g5s5AGTgP1JxYQtwQnc1m+6pWGx4fYpzskoZHcInm2A5SEwkH81DyiqL29QkPpGB6+9SEw8fcj4f9aEXb4OcxL1vTZwq1GOJ1sF0j8kpZsohO04wggQxblGlHPQNw9JS4+emmF7WL1YAdU+l28BZVwunagUCTovb17+1wS1rzGuhji2aS35HKRLg9kiEb9hCseqGCBYSQqtOOOJOyKw1h8V5JZFjOn6nBxEUnLaKF31xQgkhFM/Frf3hSkchGmjhvrsubGA==~-1~-1~1697450563; .themeshade=light; ak_bmsc=198021C245370F02DCEE9A8D057EE673~000000000000000000000000000000~YAAQH/ptaCZ7ey+OAQAA0AOnWhfTNgCQKHx4GaOCLtf86I5Q0K6b1BV2Lhz1CqQy3dWWKGeHyOnrHC+seYV9YnoMf72NJTA4dzys3ig0GC5+Awy9LyzCWJ9BajYD5Xw8VRZTIMxPud+DRTF4QMKzOdyAnAOuzSrXz08mwMujhdPjY3ikLV300cgAeI3oLmgPDEgPofaezSqICK5k225tisc3W+xe9bArP3kodEXEFVwS+pwLbCE+eSCXV6/eBe7+Jp5JW8ZAq1w0uMPXR5qTpamsU8N6PwwxgURwfneuuqDOOtgU0AQQrLgXeDdszG9Q1gQsCd08IEAXch90yAXwbN2xRwuQLNSUT9FRtgRlbE9tNx4aUYHP1jqc+SskNgKKlUwXPqBEwUvvW/0=; .ub.ses.b30a=*; .sid=89c88941-3dd8-4ace-a145-474235f2cc5c; RecentlyVisitedProducts_=20796396,37936807,38699113,21987319,7950795,20796295,37936810,21437160,21437153,21437164,22465872,22465875,18863899,18863890,18863778,20137845,14962021,3517140,3517141,9398808,13366514,16544031,22605296,22605293,39243449,32960864,38606693,38606678,40871439,8620867,14521291,14365363,36290402,724914,35624768,23253713,23253712,11056540,13987917,13987916,13987918,13410231,32960859,22605297,9104879,12098786,17763825,37059050,5609684,20688657,25053454,32837080,10397295,37936675,42390585; bm_mi=62E4B34B10EF6760C0EA14D7DFBF13E2~YAAQH/ptaKLSey+OAQAAwsOwWhd1RE4dhGVUFX3iypXv8J/0Uv2WGKp4EYbX01f8VODLFZCtGIVjpaJoUGhJtFD+eDROIfvGfIZ5vyhaqu9s/J42Nlq+ucA/nnuytyVpUVEY2Aj2unEk80x7n0t/VvOoxy2z77fQFgXGQMwkIfE3kWTPWxbzIQhna7O12AysoIn7YNr7tIEXL8CHEP/XGiVoz8K/Xlsw3ehjxmgP1rg3A50q+hKAgFjV9IqVsqJxkD7W7ZOQrMI5InlM+Qabbp5hkkurlOgEyEcppAAWdAsVMBJBs0EDtq3pD6WN1JbnVDT9gLeDCJrFPrZB1bjKMgjLeeI3ZVWYmAHfxVnz/6EIYxAMmFKUE3zY9X4MSjgUITo7hCRDRqPaIt0Az/GsvQEQjCy6fEJwY7zmoA6nCns=~1; .sidexp=1710925718; .bidexp=2026451318; bm_sv=96E9489078B8D507EFBC2F207CA1A886~YAAQH/ptaPHTey+OAQAAu+CwWhc9AM9XRPE202cv/Kjt8WDujmDXU5LZYuPeSmrhXLujeezMJuUu99SR4Fgbocs7lsS3YjmXdH1e2J4YuVrIUza9/pdsqrlfpvs7ZriEA73a+C+8W1g+hj2ABdnoawzVPHMP9eh42nHCrO3/NH6X4NJaqKczxCz8+64NxZRmrJbHG0/+cUlqjTOwdFTXIB2wpk3/bfrPnpN+Ytq3Ecp9gF4Mn/mfV+ArLOTi3vEvQA==~1; .ub.id.b30a=b449eccc-3582-41d9-9e52-9bb94bdec725.1694528816.134.1710918531.1710883565.71bbbd79-65ad-4fef-bb7f-a8711bf70315.fbcde613-72c8-425b-94b3-bad130314d97.108dd2ae-bfd3-44c7-a438-bb3e07269529.1710917880066.13; _dd_s=logs=0&expire=1710919430428',
    "origin": "https://www.digitec.ch",
    "pragma": "no-cache",
    "referer": "https://www.digitec.ch/de/s1/product/dji-mini-3-pro-mit-rc-controller-34-min-249-g-48-mpx-drohne-20796396?ip=dji+",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"122.0.6261.69"',
    "sec-ch-ua-full-version-list": '"Chromium";v="122.0.6261.69", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.69"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Linux"',
    "sec-ch-ua-platform-version": '"6.5.0"',
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "x-dg-language": "de-CH",
    "x-dg-portal": "25",
    "x-dg-routename": "/productDetail",
    "x-dg-scrumteam": "Isotopes",
}

json_data = [
    {
        "operationName": "GET_PRODUCT_DETAILS_STRUCTURED_DATA",
        "variables": {
            "productId": 20796396,
            "shopOfferId": None,
        },
        "query": "query GET_PRODUCT_DETAILS_STRUCTURED_DATA($productId: Int!, $shopOfferId: Int) {\n  productDetailsStructuredData(productId: $productId, shopOfferId: $shopOfferId)\n}",
    },
]

response = requests.post(
    "https://www.digitec.ch/api/graphql/get-product-details-structured-data",
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(json_data)
