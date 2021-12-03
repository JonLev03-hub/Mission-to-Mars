# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
df = pd.read_html('https://galaxyfacts-mars.com')[0]

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df.to_html()

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image objects from the html
html = browser.html
html_soup = soup(html, "html.parser")
find_images = html_soup.find_all('div',class_="item")

# Create dictionary objects to collect image titles and image links
for item in find_images:
    item_object = {}
    # grab the title for each image
    item_object["title"] = item.find('h3').text
    
    #Build the image url 
    url = f'https://marshemispheres.com/{item.find("a").get("href")}'
    browser.visit(url)
    temp_html = browser.html
    temp_soup = soup(temp_html,"html.parser")
    find_ = temp_soup.find('div',class_ = "downloads")
    item_object["img_url"] = f"https://marshemispheres.com/{find_.find('a').get('href')}"
    browser.back()
    hemisphere_image_urls.append(item_object)
# 5. Quit the browser
browser.quit()
print(hemisphere_image_urls)





