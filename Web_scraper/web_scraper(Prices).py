import requests
from bs4 import BeautifulSoup
import pandas as pd

# Search product
product = "laptop"

# Step 1: Get live exchange rates (USD → KES and USD → TZS)
rate_url = "https://api.exchangerate-api.com/v4/latest/USD"
rates = requests.get(rate_url).json()

usd_to_kes = rates["rates"]["KES"]
usd_to_tzs = rates["rates"]["TZS"]

# Step 2: Scrape Jumia Kenya
url = f"https://www.jumia.co.ke/catalog/?q={product}"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
items = soup.find_all("article", class_="prd")

data_list = []  # Will store spreadsheet rows

if not items:
    print("No products found or Jumia layout changed.")
else:
    print(f"\nPrices for: {product.upper()} (Converted to Tanzanian Shillings)\n")
    print(f"Exchange Rates → 1 USD = {usd_to_kes:.2f} KES, 1 USD = {usd_to_tzs:.2f} TZS\n")

    for item in items[:10]:
        name = item.find("h3", class_="name").text.strip()
        price_text = item.find("div", class_="prc").text.strip()

        # Extract numbers only
        price_kes = int("".join(filter(str.isdigit, price_text)))

        # Convert price to TZS
        price_tzs = (price_kes / usd_to_kes) * usd_to_tzs

        print(f"{name} → {price_text} (KES) ≈ {int(price_tzs):,} TZS")

        # Add to list for Excel
        data_list.append([name, price_kes, int(price_tzs)])

# Step 3: Save to Excel
df = pd.DataFrame(data_list, columns=["Product", "Price (KES)", "Price (TZS)"])
df.to_excel("prices.xlsx", index=False)

print("\n✅ Data saved to: prices.xlsx")
