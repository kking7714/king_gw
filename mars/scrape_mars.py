import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests as request
import pandas as pd
import pymongo

def scrape():
    #---Gathering mars news---
    #Use beautifulsoup to parse the site 
    url = 'https://mars.nasa.gov/news/'
    response = request.get(url)
    soup = bs(response.text,'html.parser')
    #Gather most recent title and article description
    results = soup.find(class_ = "slide")
    description = soup.find(class_ = "rollover_description_inner")
    title = soup.find(class_ = "content_title")

    #News Title and Paragraph variables
    news_title = title.text.replace('\n','').replace('\r','')
    news_p = description.text.replace('\n','').replace('\r','')
    time.sleep(2)
    #---------------------------------------#
    #---Gathering image urls from JPL NASA site---
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    jpl_response = request.get(jpl_url)
    jpl_soup = bs(jpl_response.text,'html.parser')
    #Gather image urls from the jpl site
    jpl = jpl_soup.find_all(class_ = 'img')
    url_list = []
    for j in jpl:
        pl = j.find('img')['src']
        img_urls = jpl_url + pl
        url_list.append(img_urls)
    #Featured image url variable
    featured_image_url = url_list[0]
    time.sleep(2)
    #---------------------------------------#
    #---Gathering mars weather from twitter---
    #Visit the mars twitter page and gather the latest weather content
    mars_tweet_url = 'https://twitter.com/marswxreport?lang=en'
    mars_response = request.get(mars_tweet_url)
    tweet_soup = bs(mars_response.text,'html.parser')
    # print(tweet_soup.prettify())
    tweets = tweet_soup.find_all(class_ = 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    wx = []
    for t in tweets:
        if 'daylight' in t.text:
            wx.append(t.text)
    #Mars weather variable
    mars_weather = wx[0]
    time.sleep(2)
    #---------------------------------------#
    #---Gathering mars facts as an html table---
    #Visit mars space facts page and gather table data
    mars_facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_facts_url)

    df = tables[0]
    cols = list(df[0])
    data = list(df[1])

    mars_dict = {'description':cols,'value':data}
    mars_df = pd.DataFrame(mars_dict)
    mars_df.set_index('description',inplace=True)
    mars_table = mars_df.to_html()
    #table stored as an html string with \n removed
    mars_string = mars_table.replace('\n','')
    time.sleep(2)
    #---------------------------------------#
    #---Defining Mars Hemisphere images and inserting into mongo---
    scraped_data = [
    {"title": "Cerberus Hemisphere", "imgurl": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "imgurl":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "imgurl": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hempisphere", "imgurl":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {'wx': mars_weather},
    {'facts':mars_string},
    {'ftr_img':featured_image_url},
    {'news_title':news_title, 'news_par':news_p}
    ]
    # Insert mars hemisphere information in to a Mongo DB
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.marsdb
    # scraped = build_data(scraped_data)
    return scraped_data

# def build_data(scraped_data):
#     conn = 'mongodb://localhost:27017'
#     client = pymongo.MongoClient(conn)
#     db = client.marsdb
#     collections = db.items
#     for x in scraped_data:
#         collections.insert_one(x)