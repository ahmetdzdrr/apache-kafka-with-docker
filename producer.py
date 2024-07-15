import requests
from bs4 import BeautifulSoup
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

url = 'https://scrapeme.live/shop/'

def scrape_and_send():
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')

        for link in links:
            product_url = link['href']
            product_response = requests.get(product_url)
            product_soup = BeautifulSoup(product_response.content, 'html.parser')

            title = product_soup.find('h1', class_='product_title').text.strip()
            price = product_soup.find('p', class_='price').text.strip()
            short_description = product_soup.find('div', class_='woocommerce-product-details__short-description').find('p').text.strip()
            stock_info = product_soup.find('p', class_="stock").text.strip()

            product = {
                'name': title,
                'price': price,
                'short_description': short_description,
                'stock': stock_info
            }

            producer.send('topic3', value=product)
            time.sleep(1)

        producer.flush()

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_and_send()
