import requests
from bs4 import BeautifulSoup

def main(URL):
    with open("out.csv", "a", newline="") as file: 
        headers = {'User-Agent': 'Mozilla/5.0 ...'} 
        try:
            response = requests.get(URL, headers=headers)
            response.raise_for_status()  

            soup = BeautifulSoup(response.content, "lxml")

            title_string = soup.find("span", id="productTitle").get_text(strip=True).replace(",", "") or "NA"
            price = soup.find("span", id="priceblock_ourprice").get_text(strip=True).replace(",", "") or "NA"
            rating = soup.find("i", class_="a-icon-star-4-5").get_text(strip=True) or soup.find("span", class_="a-icon-alt").get_text(strip=True).replace(",", "") or "NA"
            review_count = soup.find("span", id="acrCustomerReviewText").get_text(strip=True).replace(",", "") or "NA"
            available = soup.find("span", id="availability").get_text(strip=True).replace(",", "") or "NA"

            print("Product Title:", title_string)
            print("Product Price:", price)
            print("Overall Rating:", rating)
            print("Total Reviews:", review_count)
            print("Availability:", available)

            file.write(f"{title_string},{price},{rating},{review_count},{available}\n")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")

if __name__ == '__main__':
    with open("url.txt", "r") as url_file:
        for link in url_file:
            main(link.strip())  
