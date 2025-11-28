from flask import Flask, render_template, request
import pandas as pd
import json

app = Flask(__name__)

# ---------- BRAND DATA FILES ----------
brand_files = {
    "Mahindra": "../data/Mahindra_cars_collection_Mumbai.csv",
    "Toyota": "../data/Toyota_cars_collection_Mumbai.csv",
    "Kia": "../data/Kia_cars_collection_Mumbai.csv"
}


# Load brand dataset
def load_brand(brand):
    return pd.read_csv(brand_files[brand])


@app.route('/', methods=['GET'])
def home():

    # Selected brand (default = Mahindra)
    selected_brand = request.args.get('brand', 'Mahindra')
    df = load_brand(selected_brand)
    data = df.copy()

    # ----------- FILTERS -----------
    search = request.args.get('search', '')
    fuel = request.args.get('fuel', '')
    trans = request.args.get('trans', '')
    owners = request.args.get('owners', '')
    sort = request.args.get('sort', '')

    if search:
        data = data[data['Name'].str.contains(search, case=False)]
    if fuel:
        data = data[data['Fuel Type'] == fuel]
    if trans:
        data = data[data['Transmission'] == trans]
    if owners:
        data = data[data['Number of owners'] == int(owners)]

    # ----------- SORTING -----------
    if sort == "price_asc":
        data = data.sort_values("Price")
    elif sort == "price_desc":
        data = data.sort_values("Price", ascending=False)
    elif sort == "km_asc":
        data = data.sort_values("Kilometers Driven")
    elif sort == "km_desc":
        data = data.sort_values("Kilometers Driven", ascending=False)
    elif sort == "year_asc":
        data = data.sort_values("Year of Manufacture")
    elif sort == "year_desc":
        data = data.sort_values("Year of Manufacture", ascending=False)

    # ----------- MAIN CHART DATA -----------
    year_group = (
        data.groupby("Year of Manufacture")
            .size()
            .reset_index(name="count")
    )

    fuel_group = (
        data.groupby("Fuel Type")
            .size()
            .reset_index(name="count")
    )

    scatter_data = {
        "km": data["Kilometers Driven"].astype(int).tolist(),
        "price": data["Price"].astype(int).tolist()
    }

    # ----------- BRAND COMPARISON DATA -----------
    dfs = {
        "Mahindra": pd.read_csv("../data/Mahindra_cars_collection_Mumbai.csv"),
        "Toyota": pd.read_csv("../data/Toyota_cars_collection_Mumbai.csv"),
        "Kia": pd.read_csv("../data/Kia_cars_collection_Mumbai.csv")
    }

    # AVG PRICE
    compare_avg_price = {
        "brands": [],
        "avg_price": []
    }

    # CAR COUNT
    compare_car_count = {
        "brands": [],
        "counts": []
    }

    # FUEL STACKED BAR DATA
    fuel_stack = {}

    for brand, dfb in dfs.items():

        compare_avg_price["brands"].append(brand)
        compare_avg_price["avg_price"].append(int(dfb["Price"].mean()))

        compare_car_count["brands"].append(brand)
        compare_car_count["counts"].append(len(dfb))

        fuel_counts = dfb["Fuel Type"].value_counts().to_dict()
        for fuel_type, ct in fuel_counts.items():
            fuel_stack.setdefault(fuel_type, []).append(ct)

    compare_fuel = []
    for fuel_type, values in fuel_stack.items():
        compare_fuel.append({
            "x": list(dfs.keys()),
            "y": values,
            "name": fuel_type,
            "type": "bar"
        })

    # ----------- RENDER TEMPLATE -----------
    return render_template(
        'index.html',

        # Brand selection
        brand_list=list(brand_files.keys()),
        selected_brand=selected_brand,

        # Table
        tables=data.to_dict(orient="records"),

        # Filters
        fuel_list=sorted(df['Fuel Type'].unique()),
        trans_list=sorted(df['Transmission'].unique()),
        owner_list=sorted(df['Number of owners'].unique()),

        # Main charts
        year_labels=year_group["Year of Manufacture"].astype(int).tolist(),
        year_values=year_group["count"].astype(int).tolist(),
        fuel_labels=fuel_group["Fuel Type"].tolist(),
        fuel_values=fuel_group["count"].astype(int).tolist(),
        scatter_data=scatter_data,

        # Comparison charts
        compare_avg_price=compare_avg_price,
        compare_car_count=compare_car_count,
        compare_fuel=compare_fuel
    )


if __name__ == "__main__":
    app.run(debug=True)
