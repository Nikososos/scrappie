from bs4 import BeautifulSoup
import requests

url = "https://www.geeksforgeeks.org/"

page = requests.get(url)
print(f"The status of your site is: {page}")

soup = BeautifulSoup(page.text, features="html.parser")
# print(soup.prettify)

def checkLinks(link):
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        if response.status_code < 400:
            return "Live"
        else:
            return f"Offline (Status: {response.status_code})"
    except requests.RequestException:
        return "Dead (No response)"

for link in soup.find_all("a"):
    result = checkLinks(link)
    print(f"{link.get("href")}, = {result}")