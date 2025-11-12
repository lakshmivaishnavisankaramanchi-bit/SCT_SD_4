import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Target URL (website to scrape)
url = "https://books.toscrape.com/"

# Step 2: Send request to website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all product containers
products = soup.find_all('article', class_='product_pod')

# Step 4: Extract details (Name, Price, Rating)
product_names = []
product_prices = []
product_ratings = []

for product in products:
    name = product.h3.a['title']
    price = product.find('p', class_='price_color').text
    rating = product.p['class'][1]  # Example: "One", "Two", etc.
    
    product_names.append(name)
    product_prices.append(price)
    product_ratings.append(rating)

# Step 5: Store data in pandas DataFrame
data = pd.DataFrame({
    'Product Name': product_names,
    'Price': product_prices,
    'Rating': product_ratings
})

# Step 6: Save data to CSV file
data.to_csv('products.csv', index=False)

print("✅ Data extracted and saved to 'products.csv' successfully!")