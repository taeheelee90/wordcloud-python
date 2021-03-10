# Connect to KakaoMaps - Google play store
from selenium import webdriver 
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import time


url = "https://play.google.com/store/apps/details?id=net.daum.android.map&hl=en&showAllReviews=true"

driverPath = "./mapApp_reviews/chromedriver.exe" # Chrome Driver path 
driver = webdriver.Chrome(driverPath) # Open Chrome 
driver.get(url) # Enter the url

# Loop screen scroll to retrieve 1000+ reviews
SCROLL_PAUSE_TIME = 1.5 

for i in range(6):    
    # (1) Scroll down 5 times 
    for j in range(5): 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME) 
    
    # (2) Click 'more review'
    driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()

# Retrieve 1000+ reviews
reviews = driver.find_elements_by_xpath("//span[@jsname='bN97Pc']") 


# Convert reviews to one 'text'
text = ''
for i in range(len(reviews)):
    text += reviews[i].text


# Save txt to file
with open('./review.txt','w',  -1,  encoding = 'utf-8', newline='') as f:
    f.write(text)       
    f.close()

# Create wordcloud  
stopwords = set(STOPWORDS) 
stops = ['I','am', 'is']
for i in range (len(stops)):
    stopwords.add(stops[i])
 
wordcloud = WordCloud(max_words=80, stopwords=stopwords,background_color='white').generate(text)

# Set wordcloud image
plt.figure(figsize=(10,10)) #fix image size
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis('off') 
plt.show() 
plt.savefig('./word_cloud')

