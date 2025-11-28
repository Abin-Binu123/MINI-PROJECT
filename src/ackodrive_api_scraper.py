import requests
import pandas as pd

def scrape_ackodrive_api(brand="Hyundai", city="Mumbai"):
    print(f"Scraping {brand} cars in {city} using API...")

    url = "https://webapi.ackodrive.com/api/cars/v3/search"

    params = {
        "brand": brand.lower(),
        "city": city.lower(),
        "page": 1,
        "size": 100  # get up to 100 cars
    }

    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print("Failed to fetch data:", response.status_code)
        return

    json_data = response.json()

    cars = json_data.get("data", {}).get("cars", [])

    print(f"Cars found: {len(cars)}")

    data = []

    for car in cars:
        data.append({
            "Name": car.get("modelName"),
            "Year": car.get("year"),
            "Kilometers Driven": car.get("kmDriven"),
            "Fuel Type": car.get("fuelType"),
            "Transmission": car.get("transmissionType"),
            "Owners": car.get("ownerNumber"),
            "Price": car.get("price"),
            "Location": city
        })

    df = pd.DataFrame(data)

    df.to_csv(f"data/{brand}_cars_{city}.csv", index=False)

    print(f"Saved CSV: data/{brand}_cars_{city}.csv")
    print(df.head())

    return df


if __name__ == "__main__":
    scrape_ackodrive_api("Hyundai", "Mumbai")
