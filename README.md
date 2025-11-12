# 🧠 SkillCraft Technology Internship  
### Task 4: Product Information Extractor (SCT_SD_4)

---

## 📋 Project Overview
This project is part of my virtual internship at *SkillCraft Technology*.  
In this task, I developed a *Python program* that extracts product information such as *names, prices, and ratings* from an e-commerce website and stores the data in a *structured CSV file* for further analysis.

## 🚀 Features
- Extracts *product names, prices, and ratings* automatically  
- Uses *BeautifulSoup* for HTML parsing  
- Saves the data in a *CSV file* using *Pandas*  
- Provides structured and clean output ready for analysis  

---

## 🧩 Technologies Used
- *Python 3*
- *Requests* – to fetch web pages  
- *BeautifulSoup (bs4)* – to parse HTML and extract data  
- *Pandas* – to create and export the CSV file  

---
## 🧠 Skills Gained
- Web Scraping & Data Extraction  
- HTML Structure Understanding  
- Data Cleaning and Storage  
- CSV File Handling with Pandas  

---

## 🧾 Sample Output (CSV Preview)
| Product Name              | Price  | Rating |
|---------------------------|--------|---------|
| A Light in the Attic      | £51.77 | Three   |
| Tipping the Velvet        | £53.74 | One     |
| Soumission                | £50.10 | One     |
| Sharp Objects             | £47.82 | Four    |

---

## 🧮 Code Example
```python
import requests
 bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('article', class_='product_pod')

data = []
for product in products:
    name = product.h3.a['title']
    price = product.find('p', class_='price_color').text
    rating = product.p['class'][1]
    data.append({'Product Name': name, 'Price': price, 'Rating': rating})

df = pd.DataFrame(data)
df.to_csv('products.csv', index=False)
print("✅ Data extracted and saved to products.csv successfully!")





 🏅 Internship Details
Organization: SkillCraft Technology
Internship Domain: Software Development / Data Science
Task Code: SCT_SD_4
Duration: November 2025




## Acknowledgment
Grateful to SkillCraft Technology for providing this wonderful opportunity to learn and enhance my skills in Python programming and web scraping.


---

🌐 Author:
S.LAKSHMI VAISHNAVI
https://www.linkedin.com/in/lakshmi-vaishnavi-36518a2bb?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

#SkillCraftTechnology #SCT_SD_4 #Python #WebScraping #BeautifulSoup #Pandas #Internship #DataScience #LearningByDoing
