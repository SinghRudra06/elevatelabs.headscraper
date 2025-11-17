import requests
from bs4 import BeautifulSoup


link= "https://timesofindia.indiatimes.com/"
response = requests.get(link)

if response.status_code != 200:
    print("Failed to collect the webpage")
    exit()
soup = BeautifulSoup(response.text,"html.parser")

headings_tags = ["h1","h2","h3"]

headlines=[]
for tag in soup.find_all(headings_tags):
    text = tag.get_text(strip=True)
    if text:
        headlines.append(text)

with open("newsheadline.txt","w",encoding="utf-8") as file:
    for line in headlines:
        file.write(line + "\n")
print(f"Saved {len(headlines)} headlines to newsheadlines.txt")
