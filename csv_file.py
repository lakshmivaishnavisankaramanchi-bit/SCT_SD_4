import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL (demo site safe for scraping)
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

# Get webpage data
soup = BeautifulSoup(requests.get(url).text, "html.parser")

# Extract product details
products = soup.select(".col-sm-4.col-lg-4.col-md-4")

data = []
for p in products:
    name = p.select_one(".title").text.strip()
    price = p.select_one(".price").text.strip()
    rating = p.select_one(".pull-right").text.strip()
    data.append([name, price, rating])

# Save to CSV
pd.DataFrame(data, columns=["Product Name", "Price", "Rating"]).to_csv("products.csv", index=False)

print("✅ Product data saved to products.csv successfully!")