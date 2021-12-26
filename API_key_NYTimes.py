#!/usr/bin/env python
# coding: utf-8

# In[141]:


import json
import requests
import time
import datetime


# In[117]:


end = datetime.date.today()
start = datetime.date(2021, 9, 24)
print('Start date ' + str(start))
print('End date ' + str(end))


# In[118]:


your_key = 'BwLkeqBjXh0LEKdy7mdoVKrXETtD5FG3'
url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Omicron&part=web_url,snippet&api-key='+your_key
response = requests.get(url)
json_data = response.json()
print(json_data)


# In[120]:


#Making it more easy to read
str_data = json.dumps(json_data, indent=2)
print(str_data)


# In[121]:


articles = json_data["response"]["docs"][0]


# In[122]:


print(articles)


# In[123]:


article_url = json_data["response"]["docs"][0]["web_url"]


# In[124]:


print(article_url)


# In[125]:


article_snippet = json_data["response"]["docs"][0]["snippet"]


# In[126]:


print(article_snippet)


# In[127]:


article_date = json_data["response"]["docs"][0]["pub_date"]


# In[128]:


print(article_date)


# In[109]:


article_date = str(article_date).split("T")[0]


# In[129]:


print(article_date)


# In[138]:


print(article_url)
print(article_snippet)
print(article_date)


# In[139]:


for item in json_data["response"]["docs"]:
    article_url = item["web_url"]
    article_snippet = item["snippet"]
    article_date = item["pub_date"]
    article_date = str(article_date).split("T")[0]
    print(article_url)
    print(article_snippet)
    print(article_date)


# In[142]:


import csv
file = 'omicron_search_nyt.csv'

with open(file, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)


# In[ ]:




