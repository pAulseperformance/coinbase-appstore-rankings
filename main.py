import requests
from bs4 import BeautifulSoup

# URL of Coinbase on the App Store (you'll need to adapt it based on the country/region)
url = "https://apps.apple.com/us/app/coinbase-buy-sell-crypto/id886427730"

# Send HTTP request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract ranking information
# (You need to inspect the App Store webpage and find the specific element containing the ranking)
ranking_section = soup.find('a', class_='inline-list__item', href="https://apps.apple.com/us/charts/iphone/finance-apps/6015")

if ranking_section:
    ranking = ranking_section.get_text()
    print(f"Coinbase's ranking: {ranking}")
else:
    print("Ranking not found.")
