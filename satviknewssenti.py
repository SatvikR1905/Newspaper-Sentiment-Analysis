from newspaper import Article 
import textblob

API_KEY = "3aa64de503f149cfab612ba68c850f34"
url = 'https://www.latimes.com/world-nation/story/2020-09-20/coronavirus-aerosol-airborne-spread'

my_article = Article(url, language="en")
my_article.download()
my_article.parse()
#print('Authors:',my_article.authors)
#print('Publishing date:',my_article.publish_date)
my_article.nlp()

Title = my_article.title
Summary = my_article.summary 
Keywords = my_article.keywords

blob = textblob.TextBlob(Summary)
b= blob.sentiment.polarity

senti_category = ""
if b > 0.75:
    senti_category = "Extremely positive."
elif b > 0.5:
    senti_category = "Significantly positive."
elif b > 0.3:
    senti_category = "Fairly positive."
elif b > 0.1:
    senti_category = "Slightly positive."
elif b < -0.1:
    senti_category = "Slightly negative."
elif b < -0.3:
    senti_category = "Fairly negative."
elif b < -0.5:
    senti_category = "Significantly negative."
elif b < -0.75:
    senti_category = "Extremely negative."
else:
    senti_category = "Neutral."
        
print("Title:",Title)
print("Summary:",Summary)
print("Keywords:",Keywords)
print("Polarity:",b)
print("Sentiment:",senti_category)

    




