import cloudscraper
scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'desktop': True})
urls = [
    "https://www.apkmirror.com/apk/x-corp/twitter/twitter-10-60-0-release/",
    "https://www.apkmirror.com/apk/x-corp/x/x-10-60-0-release/",
    "https://www.apkmirror.com/apk/twitter-inc/twitter/twitter-10-60-0-release/",
    "https://www.apkmirror.com/apk/twitter-inc/x/x-10-60-0-release/"
]
for u in urls:
    try:
        r = scraper.get(u)
        print(f"{u} -> {r.status_code}")
    except Exception as e:
        print(f"{u} -> ERROR")
