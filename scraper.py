import scraperwiki
import lxml.html
import requests
import json
import urllib

url = "http://www.transparencyinternational.eu/european-commissions-lobbying-meetings/"
html = requests.get(url).text
root = lxml.html.fromstring(html)
people_links = [link.get('href') for link in root.cssselect("table tr td:nth-of-type(3) a")]

for link in people_links:
  html_meetings = requests.get(link).text
  root_meetings = lxml.html.fromstring(html_meetings)
  host = root_meetings.cssselect("h3")[0].text_content().strip().encode('ascii', 'ignore')
#  try:
  number_pages = root_meetings.cssselect("span a")[-1].get('href')
  #except IndexError: 
   # number_pages = 1
  print number_pages
  
  #//*[@id="layout"]/div/div[2]/center/span[1]/a[7]

# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
