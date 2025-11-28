This project is part of the EVOASTRA Internship MINI PROJECT, focused on web scraping, data cleaning, dashboard creation, and analysis of used cars listed on AckoDrive.com.

Due to AckoDrive’s dynamic rendering and anti-scraping protections, we used a combination of:

Scraping attempts (Requests/Selenium)

Prepared datasets (Mahindra, Toyota, Kia)

Exploratory API/HTML analysis

Data visualization & brand comparison dashboard

The final deliverables include:

A full Flask dashboard

A complete Jupyter Notebook

A set of clean, structured CSV datasets

A graphical brand comparison system

📁 Project Structure
MINI PROJECT/
│
├── data/
│   ├── Mahindra_cars_collection_Mumbai.csv
│   ├── Toyota_cars_collection_Mumbai.csv
│   ├── Kia_cars_collection_Mumbai.csv
│
├── notebooks/
│   ├── Web_Scraping_MiniProject.ipynb
│   ├── Advanced_Web_Scraping_MiniProject.ipynb
│
├── src/
│   ├── app.py                # Flask dashboard backend
│   ├── generate_datasets.py  # Script for Toyata & Kia dataset generation
│   ├── templates/
│   │   └── index.html         # Dashboard UI
│
└── README.md

🎯 Project Objectives
✔ Scrape car details for Mumbai from AckoDrive
✔ Collect key fields:

Kilometers Driven

Year of Manufacture

Fuel Type

Transmission

Price

Location

Number of Owners

Brand

✔ Build complete datasets for:

Mahindra

Toyota

Kia

✔ Create a fully interactive dashboard that includes:

Filters (fuel, owners, transmission)

Sorting options

Search feature

Interactive charts:

Cars by Year

Fuel Type Distribution

Price vs KM Scatter Plot

Brand Comparison Charts

🛠 Technologies Used
Backend:

Python

Flask

Frontend:

HTML

Bootstrap

Plotly.js

Data Analysis:

Pandas

Matplotlib

Seaborn

Plotly

Notebook Environment:

Jupyter Notebook

VS Code

📊 Dashboard Features
🔍 Filters

Fuel Type

Transmission

Owners

Sort (Price, KM, Year)

Search by Car Name

Brand Dropdown (Mahindra, Toyota, Kia)

📈 Graphs

Cars by Year

Fuel Type Distribution

Price vs KM Scatter

Brand Comparison Charts:

Average Price by Brand

Car Count by Brand

Stacked Fuel Type Chart

📘 Jupyter Notebook Deliverables
The notebook includes:

Scraping attempts

Analysis of AckoDrive DOM & JS rendering

Prepared dataset loading

Cleaning pipeline

Per-brand visualizations

Brand comparison graphs

Export of combined cleaned dataset

Notebook files:

Web_Scraping_MiniProject.ipynb

Advanced_Web_Scraping_MiniProject.ipynb

🧪 How to Run the Flask App
1️⃣ Install dependencies:
pip install flask pandas plotly

2️⃣ Navigate to project folder:
cd src

3️⃣ Run the app:
python app.py

4️⃣ Visit dashboard:
http://127.0.0.1:5000/

📥 Datasets Used

All datasets are located in the data/ folder.

Mahindra (scraped/prepared)

Toyota (prepared)

Kia (prepared)

All follow the same structure to allow multi-brand comparison.

🚀 Future Enhancements

Machine Learning model: Predict used car prices

Automatic live scraping using undetected browser

Deployment to Render / Vercel

Admin panel for uploading new datasets

👨‍💻 Author / Contributors

Abin Binu
B.Tech AIML
EVOASTRA Internship Program

📝 License

This project is for educational and internship assessment purposes.
