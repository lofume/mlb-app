

from django.shortcuts import render
import xml.etree.ElementTree as ET
import requests

def fetch_news_from_feed():
    rss_url = "https://www.mlb.com/feeds/news/rss.xml"
    response = requests.get(rss_url)
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        news_data = []
        for item in root.findall(".//item"):
            title = item.find("title").text
            link = item.find("link")
            pub_date = item.find("pubDate").text
            image_url = item.find(".//image").get("href")  # Extract image URL
            
            news_data.append({
                "title": title,
                "link": link,
                "pub_date": pub_date,
                "image_url": image_url,
            })
        return news_data
    return None

def news_list(request):
    news_data = fetch_news_from_feed()
    return render(request, 'news_list.html', {'news_data': news_data})


def standings_view(request):
    # Define the API URL
    api_url = 'https://statsapi.mlb.com/api/v1/standings?leagueId=103,104'  # Replace with your API URL

    try:
        # Fetch data from the API
        response = requests.get(api_url)
        data = response.json()  # Assuming the API returns JSON data
    except requests.exceptions.RequestException as e:
        # Handle API request errors (e.g., connection error, invalid URL)
        error_message = str(e)
        data = None

    return render(request, 'standings/standings.html', {'standings_data': data, 'error_message': error_message})
