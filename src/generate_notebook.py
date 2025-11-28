import nbformat as nbf
import os

# Make notebooks folder
os.makedirs("../notebooks", exist_ok=True)

# Create notebook
nb = nbf.v4.new_notebook()

cells = []

# Title
cells.append(nbf.v4.new_markdown_cell("# Web Scraping Project – AckoDrive Car Data\n"
                                      "Mini Project – EVOASTRA Internship\n\n"
                                      "This notebook documents scraping attempts, dataset usage, "
                                      "cleaning, and analysis."))

# Objective
cells.append(nbf.v4.new_markdown_cell("## 1. Project Objective\n"
                                      "- Scrape car details from **AckoDrive.com**\n"
                                      "- Extract details: Kilometers, Year, Fuel, Transmission, Price, Location, Owners\n"
                                      "- Primary location: **Mumbai**\n"
                                      "- Save to CSV\n"
                                      "- Perform analysis & visualization"))

# Libraries
cells.append(nbf.v4.new_markdown_cell("## 2. Import Libraries"))
cells.append(nbf.v4.new_code_cell("import pandas as pd\nimport matplotlib.pyplot as plt"))

# Scraping explanation
cells.append(nbf.v4.new_markdown_cell("## 3. Understanding AckoDrive Website Behavior\n"
                                      "AckoDrive uses **dynamic JavaScript rendering + GraphQL APIs**, "
                                      "so direct HTML scraping with `requests` does not return car data.\n\n"
                                      "**Result:** Classic scraping won't work → dataset must be collected by API methods "
                                      "or pre-prepared CSV files."))

# Load dataset
cells.append(nbf.v4.new_markdown_cell("## 4. Load Prepared Dataset (Mahindra Example)"))
cells.append(nbf.v4.new_code_cell(
"""df = pd.read_csv('../data/Mahindra_cars_collection_Mumbai.csv')
df.head()"""
))

# Cleaning
cells.append(nbf.v4.new_markdown_cell("## 5. Basic Data Cleaning"))
cells.append(nbf.v4.new_code_cell(
"""df.info(), df.isna().sum()"""
))

# Visualization
cells.append(nbf.v4.new_markdown_cell("## 6. Visualization – Cars by Year"))
cells.append(nbf.v4.new_code_cell(
"""df['Year of Manufacture'].value_counts().sort_index().plot(kind='bar', figsize=(10,5))
plt.title('Cars by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()"""
))

# Save notebook
nb["cells"] = cells

output_path = "../notebooks/Web_Scraping_MiniProject.ipynb"

with open(output_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook created successfully at: {output_path}")
