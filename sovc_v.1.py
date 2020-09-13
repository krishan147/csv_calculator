import requests
import time
import json
import urllib
import urllib2
import re
import datetime
import pyodbc
import csv
import sys
from selenium import webdriver
import os
import praw

#THIS IS THE CSV FILE WITH ALL THE MENTIONS IN THEM

with open('CSV FILE.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    datalist = []
    for row in data:
        if len (row) != 0:
            datalist = datalist + [row]
csvfile.close()
column_names = datalist[0] #LIST OF COLUMNS
#FINDS THE RIGHT COLUMNS IN ORDER TO ADD UP THE BRANDS AND MARKETS YOU WANT TO ANALYSE.
final_reach_figure_list = []
these_get_added = []
#THIS IS WHERE ALL THE MARKETS ARE. NOTE THAT THESE QUERIES ARE CASE SENSITIVE!

country_list = ["gb","it","fr","es","be"]

#THESE ARE ALL THE QUERIES 

for single_country in country_list:
    drinks = {"kangeroo" : ["kangeroo", "kanggeroo", "kangreoo", "cangeroo"],
              "elephant" : ["elephant", "elefant", "ellephant", "ellefant", "ellephent"],
              "giraffe" : ["giraffe", "girafe", "jirafe", "geerafe"],
              "diplodocus" : ["diplodocus", "dipplodocus", "dipllodocus", "dipelodocus"],}
            
    for brand, query_terms in drinks.iteritems():
        for query_term in query_terms:
            for row_find in datalist:
                rows = row_find[0]
                content_snip = row_find[5]
                country = row_find[78]
                
#WORKS OUT IF QUERY TERM IS IN CONTENT SNIPPET COLUMN AND IF COUNTRY IS IN COUNTRY COLUMN IN THE EXCEL FILE                       
                if (query_term in (content_snip.lower()) and single_country in country):
                    #print brand, single_country, query_term,
                    
                #INSTAGRAM
                    
                    if "instagram" in rows:
                        insta_followers_five = 0
                        url = row_find[0]
                        domain = row_find[9]
                        host_url = row_find[10]
                        reach = row_find[84]
                        published = row_find[2]
                        url_image = row_find[25]
                        num_comments = row_find[47]
                        city = row_find[80]
                        insta_likes = row_find[45]
                        insta_handle = "handle"
                        insta_id = "insta id"
                        insta_post_id = "insta post id"

                        insta_followers = row_find[51]
                        insta_followers_five = int(insta_followers)*0.05 + 1

                        these_get_added.append(insta_followers_five)
                        insta_results = url, ",", insta_followers_five, ",", published

                #TWITTER
                        
                    elif "twitter" in rows:
                        tw_followers_five = 0
                        url = row_find[0]
                        domain = row_find[9]
                        host_url = row_find[10]
                        reach = row_find[84]
                        published = row_find[2]
                        content_snip = row_find[5]
                        url_image = row_find[25]
                        num_comments = row_find[47]
                        country = row_find[78]
                        city = row_find[80]
                        tw_handle = "handle"
                        tw_id = "fb id"
                        tw_post_id = "tw post id"
                        tw_retweets = row_find[37]
                        tw_shares = row_find[46]
                        content_snip = row_find[5]
                        tw_followers = row_find[50]
                        tw_followers_five = int(tw_followers)*0.05 + 1
                        these_get_added.append(tw_followers_five)
                        tw_results = url, ",", tw_followers_five, ",", published

                #FACEBOOK
                        
                    elif "facebook" in rows:
                        fb_followers_five = 0
                        url = row_find[0]
                        domain = row_find[9]
                        host_url = row_find[10]
                        published = row_find[2]
                        content_snip = row_find[5]
                        url_image = row_find[25]
                        num_comments = row_find[47]
                        country = row_find[78]
                        city = row_find[80]
                        fb_handle = "handle"
                        fb_id = "fb id"
                        fb_post_id = "fb post id"
                        fb_shares = row_find[35]
                        fb_likes = row_find[36]
                        fb_followers = row_find[49]
                        fb_followers_five = int(fb_followers)*0.05 + 1
                        these_get_added.append(fb_followers_five)
                        fb_results = url, ",", fb_followers_five, ",", published

                #REDDIT
                        
                    elif "reddit" in rows:
                        try:
                            reddit_url_dirty_start = rows.find("/r/")
                            reddit_url_dirty_end = rows.find("/comments")
                            subreddit_r = rows[reddit_url_dirty_start:reddit_url_dirty_end]
                            subreddit = subreddit_r.replace("/r/","")
                            published = row_find[2]
                            time.sleep(10)
                            my_user_agent = 'INSERT USER NAME'
                            my_client_id = 'INSERT CLIENT ID'
                            my_client_secret = 'INSERT CLIENT SECRET'
                            reddit = praw.Reddit(user_agent=my_user_agent,client_id=my_client_id,client_secret=my_client_secret)
                            subreddit = reddit.subreddit(subreddit)
                            reddit_subscribers = subreddit.subscribers
                            full_subreddit_link = "https://www.reddit.com/r/"+str(subreddit)+"/"
                            reddit_subscribers_five = reddit_subscribers*0.05 + 1
                            these_get_added.append(reddit_subscribers_five)
                            reddit_results = full_subreddit_link, ",", reddit_subscribers_five, ",", published, ",", subreddit
                        except:
                            pass

                #BLOGSPOT
                    elif "blogspot" in rows:
                        pass
##                        try:
##                            url = row_find[0]
##                            published = row_find[2]
##                            driver = webdriver.Chrome()
##                            driver.get(url)
##                            driver.switch_to_frame(driver.find_element_by_xpath('//div[@id="followers-iframe-container"]/iframe'))
##                            followers_text = driver.find_element_by_xpath('//div[@class="member-title"]').text
##                            followers = int(followers_text.split('(')[1].split(')')[0])
##                            blogspot_followers_five = followers*0.05 + 1
##
##                            time.sleep(4)
##                            driver.quit()
##                            time.sleep(2)
##                            these_get_added.append(blogspot_followers_five)
##                            blogspot_results = url, ",",blogspot_followers_five,",",published
##                        except:
##                            driver = webdriver.Chrome()
##                            time.sleep(4)
##                            driver.quit()
##                            time.sleep(2)
##                            pass

                    #OTHER SITES TO PASS

                    elif "youtube" in rows:
                        pass
                    elif "wikipedia" in rows:
                        pass
                    elif "kindlescout" in rows:
                        pass
                    elif "amazon" in rows:
                        pass
                    elif "vk.com" in rows:
                        pass
                    elif "amazon" in rows:
                        pass
                    elif "wordpress" in rows:
                        pass
                    elif "tumblr" in rows:
                        pass
                    elif "pinterest" in rows:
                        pass
                    elif "flickr" in rows:
                        pass
     
                #OTHER      
                    else:
                        url = row_find[0]
                        domain = row_find[9]
                        root_url = row_find[10]
                        published = row_find[2]
                        content_snip = row_find[5]
                        url_image = row_find[25]
                        num_comments = row_find[47]
                        country = row_find[78]
                        city = row_find[80]
                        title_snip = row_find[4]
                        content_snip = row_find[5]

                        reach = row_find[84]

                        http_root_url = root_url.replace("https","http")

                        database_details = 'DRIVER={SQL Server};SERVER=ENTER SERVER NAME;DATABASE=ENTER DATABASE NAME;UID=ENTER USER ID;PWD=ENTER PASSWORD'
                        table_name = 'Aleksa_two'

                        cnxn = pyodbc.connect(database_details)
                        cursor = cnxn.cursor()
                        cursor.execute("select url, reach_five_percent from "+table_name+" WHERE url IS NOT NULL")
                        aleksa_url = cursor.fetchall()
                        for data in aleksa_url:
                            url_compare = data[0]
                            reach_five = data[1]
                            reach_five_int = int(reach_five)
                            if http_root_url in url_compare:
                                other_results = http_root_url, ",", reach_five_int, ",", published
                                these_get_added.append(reach_five_int)
                            else:
                                pass
                        
                    final_reach_figure = sum(i for i in these_get_added)
                    final_reach_figure_list = []
                    final_reach_figure_list.append(final_reach_figure)

############################################################################################################################################################################################################################
##
#UNCOMMENT THE CODE BELOW IN ORDER TO SEE WHAT IS RESPONSIBLE FOR MAKING THE REACH 
##
##                    
##                    try:
##                        if insta_followers_five:
##                            print brand, "," ,single_country, "," ,len(these_get_added), ",",insta_followers_five,"," ,final_reach_figure, "," ,query_term, "," ,url
##                        if tw_followers_five:
##                            print brand, "," ,single_country, "," ,len(these_get_added), ",",tw_followers_five,"," ,final_reach_figure, "," ,query_term, "," ,url
##                        if fb_followers_five:
##                            print brand, "," ,single_country, "," ,len(these_get_added), ",",fb_followers_five,"," ,final_reach_figure, "," ,query_term, "," ,url
##                        if reddit_subscribers_five:
##                            print brand, "," ,single_country, "," ,len(these_get_added), ",",reddit_subscribers_five,"," ,final_reach_figure, "," ,query_term, "," ,url
##                        if reach_five_int:
##                            print brand, "," ,single_country, "," ,len(these_get_added), ",",reach_five_int,"," ,final_reach_figure, "," ,query_term, "," ,url
##                    except:
##                        pass
##                            
############################################################################################################################################################################################################################
                    
        print "BRAND:"+str(brand)+","+"COUNTRY:"+str(single_country)+","+"NUM OF MENTIONS:"+str(len(these_get_added))+","+"REACH:"+str(final_reach_figure_list)
        these_get_added = []

                   
                        
                    

