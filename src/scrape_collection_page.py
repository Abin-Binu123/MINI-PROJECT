import json
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def scrape_collection_page():
    url = "https://ackodrive.com/collection/mahindra+cars/"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print("Opening page:", url)
    driver.get(url)

    time.sleep(5)

    # get page source
    html = driver.page_source

    driver.quit()

    # find JSON block inside script tag
    key = "__APP_INITIAL_STATE__"
    start = html.find(key)

    if start == -1:
        print("❌ Could not find embedded JSON")
        return

    # extract JSON (starts after "key = ")
    start = html.find("{", start)
    end = html.find("</script>", start)

    raw_json = html[start:end]

    # Fix invalid JS to JSON
    raw_json = raw_json.replace("undefined", "null")

    try:
        data = json.loads(raw_json)
    except Exception as e:
        print("JSON decode error:", e)
        return

    # Navigate inside JSON to car list
    cars = data["entities"]["inventory"]["items"]

    rows = []
    for cid, info in cars.items():
        rows.append({
            "Car ID": cid,
            "Name": info.get("title"),
            "Price": info.get("price"),
            "Fuel": info.get("fuelType"),
            "Transmission": info.get("transmissionType"),
            "Image URL": info.get("imageUrl"),
            "Body Type": info.get("bodyType"),
            "Location": "India",
        })

    df = pd.DataFrame(rows)
    df.to_csv("data/Mahindra_cars_Mumbai.csv", index=False)

    print("\n✔ Saved: data/Mahindra_cars_Mumbai.csv")
    print(df.head())

if __name__ == "__main__":
    scrape_collection_page()
