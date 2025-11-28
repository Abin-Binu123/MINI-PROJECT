import requests
import pandas as pd

def scrape_ackodrive_graphql(brand="Hyundai", city="Mumbai"):
    print(f"Scraping {brand} cars in {city} using GraphQL API...")

    url = "https://webapi.ackodrive.com/graphql"

    # GraphQL Query
    query = """
    query UsedCars($brand: String!, $city: String!) {
      usedCars(
        filters: { brand: [$brand], city: $city }
        pagination: { page: 1, size: 100 }
      ) {
        cars {
          modelName
          year
          kmDriven
          fuelType
          transmissionType
          ownerNumber
          price
        }
      }
    }
    """

    variables = {
        "brand": brand.lower(),
        "city": city.lower()
    }

    response = requests.post(url, json={"query": query, "variables": variables})

    if response.status_code != 200:
        print("❌ Failed:", response.status_code)
        return None

    data = response.json()

    if "errors" in data:
        print("❌ GraphQL Error:", data["errors"])
        return None

    cars = data["data"]["usedCars"]["cars"]

    rows = []
    for c in cars:
        rows.append({
            "Name": c["modelName"],
            "Year": c["year"],
            "Kilometers Driven": c["kmDriven"],
            "Fuel Type": c["fuelType"],
            "Transmission": c["transmissionType"],
            "Owners": c["ownerNumber"],
            "Price": c["price"],
            "Location": city
        })

    df = pd.DataFrame(rows)
    df.to_csv(f"data/{brand}_cars_{city}.csv", index=False)

    print(f"✔ CSV Saved: data/{brand}_cars_{city}.csv")
    print(df.head())

    return df


if __name__ == "__main__":
    scrape_ackodrive_graphql("Hyundai", "Mumbai")
