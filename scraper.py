import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_articles(max_articles=30):
    base_urls = {
        "Optimism": "https://gov.optimism.io/",
        "Arbitrum": "https://forum.arbitrum.foundation/categories"
    }

    articles = []
    for category, url in base_urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        category_elements = soup.find_all("td", class_="category")

        for cat in category_elements:
            if len(articles) >= max_articles:
                break
            link_tag = cat.find("a")
            category_link = f"{url}{link_tag['href']}" if link_tag else None
            category_name = cat.find("span", itemprop="name").text.strip() if cat.find("span", itemprop="name") else None

            if category_link:
                response = requests.get(category_link)
                category_soup = BeautifulSoup(response.content, "html.parser")
                article_elements = category_soup.find_all("a", class_="title")

                for article in article_elements:
                    if len(articles) >= max_articles:
                        break
                    article_link = f"{url}{article['href']}" if article else None
                    article_title = article.text.strip() if article else None

                    articles.append({
                        "Category Name": category_name,
                        "Link": article_link,
                        "Description": article_title
                    })

    return pd.DataFrame(articles)
