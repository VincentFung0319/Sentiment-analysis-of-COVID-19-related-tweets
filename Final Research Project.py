import sentiment_mod as s
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker
from matplotlib import style
import time
import pandas as pd
import glob
from textblob import TextBlob
import re
import string
import nltk
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.corpus import stopwords
import os
import csv
from sklearn.feature_extraction.text import CountVectorizer

'''
Delete the column of sentiment score and hydrate the tweet IDs
'''
path = '/Volumes/Vincent/COVID19 Tweets/Tweets with text/CSV file/first wave of covid19/'
path2 = '/Volumes/Vincent/COVID19 Tweets/Tweets with text/CSV file/second wave of covid19/'

files = []

for file in os.listdir(path):
    if file.endswith(".csv"):
        files.append(path+file)

for file in files:
    dataFrame = pd.read_csv(file, header=None)
    dataFrame = dataFrame[0]
    dataFrame.to_csv(file, index=False, header=None)

for file in os.listdir(path2):
    if file.endswith(".csv"):
        files.append(path2+file)

for file in files:
    dataFrame = pd.read_csv(file, header=None)
    dataFrame = dataFrame[0]
    dataFrame.to_csv(file, index=False, header=None)


'''
Read the daily tweets of the first wave of covid19 (03.20 ~ 06.30)
'''
tweet0320_p1 = pd.read_csv(path + 'corona_tweets_0320_p1.csv')
tweet0320_p2 = pd.read_csv(path + 'corona_tweets_0320_p2.csv')
tweet0320_p3 = pd.read_csv(path + 'corona_tweets_0320_p3.csv')
tweet0321 = pd.read_csv(path + 'corona_tweets_0321.csv')
tweet0322 = pd.read_csv(path + 'corona_tweets_0322.csv')
tweet0323 = pd.read_csv(path + 'corona_tweets_0323.csv')
tweet0324 = pd.read_csv(path + 'corona_tweets_0324.csv')
tweet0325 = pd.read_csv(path + 'corona_tweets_0325.csv')
tweet0326 = pd.read_csv(path + 'corona_tweets_0326.csv')
tweet0327 = pd.read_csv(path + 'corona_tweets_0327.csv')
tweet0328 = pd.read_csv(path + 'corona_tweets_0328.csv')
tweet0330 = pd.read_csv(path + 'corona_tweets_0330.csv')
tweet0331 = pd.read_csv(path + 'corona_tweets_0331.csv')
tweet0401 = pd.read_csv(path + 'corona_tweets_0401.csv')
tweet0402 = pd.read_csv(path + 'corona_tweets_0402.csv')
tweet0403 = pd.read_csv(path + 'corona_tweets_0403.csv')
tweet0404 = pd.read_csv(path + 'corona_tweets_0404.csv')
tweet0405 = pd.read_csv(path + 'corona_tweets_0405.csv')
tweet0406 = pd.read_csv(path + 'corona_tweets_0406.csv')
tweet0407 = pd.read_csv(path + 'corona_tweets_0407.csv')
tweet0408 = pd.read_csv(path + 'corona_tweets_0408.csv')
tweet0409 = pd.read_csv(path + 'corona_tweets_0409.csv')
tweet0410 = pd.read_csv(path + 'corona_tweets_0410.csv')
tweet0411 = pd.read_csv(path + 'corona_tweets_0411.csv')
tweet0412 = pd.read_csv(path + 'corona_tweets_0412.csv')
tweet0413 = pd.read_csv(path + 'corona_tweets_0413.csv')
tweet0414 = pd.read_csv(path + 'corona_tweets_0414.csv')
tweet0415 = pd.read_csv(path + 'corona_tweets_0415.csv')
tweet0416 = pd.read_csv(path + 'corona_tweets_0416.csv')
tweet0417 = pd.read_csv(path + 'corona_tweets_0417.csv')
tweet0418 = pd.read_csv(path + 'corona_tweets_0418.csv')
tweet0419 = pd.read_csv(path + 'corona_tweets_0419.csv')
tweet0420 = pd.read_csv(path + 'corona_tweets_0420.csv')
tweet0421 = pd.read_csv(path + 'corona_tweets_0421.csv')
tweet0422 = pd.read_csv(path + 'corona_tweets_0422.csv')
tweet0423 = pd.read_csv(path + 'corona_tweets_0423.csv')
tweet0424 = pd.read_csv(path + 'corona_tweets_0424.csv')
tweet0425 = pd.read_csv(path + 'corona_tweets_0425.csv')
tweet0426 = pd.read_csv(path + 'corona_tweets_0426.csv')
tweet0427 = pd.read_csv(path + 'corona_tweets_0427.csv')
tweet0428 = pd.read_csv(path + 'corona_tweets_0428.csv')
tweet0429 = pd.read_csv(path + 'corona_tweets_0429.csv')
tweet0430 = pd.read_csv(path + 'corona_tweets_0430.csv')
tweet0501 = pd.read_csv(path + 'corona_tweets_0501.csv')
tweet0502 = pd.read_csv(path + 'corona_tweets_0502.csv')
tweet0503 = pd.read_csv(path + 'corona_tweets_0503.csv')
tweet0504 = pd.read_csv(path + 'corona_tweets_0504.csv')
tweet0505 = pd.read_csv(path + 'corona_tweets_0505.csv')
tweet0506 = pd.read_csv(path + 'corona_tweets_0506.csv')
tweet0507 = pd.read_csv(path + 'corona_tweets_0507.csv')
tweet0508 = pd.read_csv(path + 'corona_tweets_0508.csv')
tweet0509 = pd.read_csv(path + 'corona_tweets_0509.csv')
tweet0510 = pd.read_csv(path + 'corona_tweets_0510.csv')
tweet0511 = pd.read_csv(path + 'corona_tweets_0511.csv')
tweet0512 = pd.read_csv(path + 'corona_tweets_0512.csv')
tweet0513 = pd.read_csv(path + 'corona_tweets_0513.csv')
tweet0514 = pd.read_csv(path + 'corona_tweets_0514.csv')
tweet0515 = pd.read_csv(path + 'corona_tweets_0515.csv')
tweet0516 = pd.read_csv(path + 'corona_tweets_0516.csv')
tweet0517 = pd.read_csv(path + 'corona_tweets_0517.csv')
tweet0518 = pd.read_csv(path + 'corona_tweets_0518.csv')
tweet0519 = pd.read_csv(path + 'corona_tweets_0519.csv')
tweet0520 = pd.read_csv(path + 'corona_tweets_0520.csv')
tweet0521 = pd.read_csv(path + 'corona_tweets_0521.csv')
tweet0522 = pd.read_csv(path + 'corona_tweets_0522.csv')
tweet0523 = pd.read_csv(path + 'corona_tweets_0523.csv')
tweet0524 = pd.read_csv(path + 'corona_tweets_0524.csv')
tweet0525 = pd.read_csv(path + 'corona_tweets_0525.csv')
tweet0526 = pd.read_csv(path + 'corona_tweets_0526.csv')
tweet0527 = pd.read_csv(path + 'corona_tweets_0527.csv')
tweet0528 = pd.read_csv(path + 'corona_tweets_0528.csv')
tweet0529 = pd.read_csv(path + 'corona_tweets_0529.csv')
tweet0530 = pd.read_csv(path + 'corona_tweets_0530.csv')
tweet0531 = pd.read_csv(path + 'corona_tweets_0531.csv')
tweet0601 = pd.read_csv(path + 'corona_tweets_0601.csv')
tweet0602 = pd.read_csv(path + 'corona_tweets_0602.csv')
tweet0603 = pd.read_csv(path + 'corona_tweets_0603.csv')
tweet0604 = pd.read_csv(path + 'corona_tweets_0604.csv')
tweet0605 = pd.read_csv(path + 'corona_tweets_0605.csv')
tweet0606 = pd.read_csv(path + 'corona_tweets_0606.csv')
tweet0607 = pd.read_csv(path + 'corona_tweets_0607.csv')
tweet0608 = pd.read_csv(path + 'corona_tweets_0608.csv')
tweet0609 = pd.read_csv(path + 'corona_tweets_0609.csv')
tweet0610 = pd.read_csv(path + 'corona_tweets_0610.csv')
tweet0611 = pd.read_csv(path + 'corona_tweets_0611.csv')
tweet0612 = pd.read_csv(path + 'corona_tweets_0612.csv')
tweet0613 = pd.read_csv(path + 'corona_tweets_0613.csv')
tweet0614 = pd.read_csv(path + 'corona_tweets_0614.csv')
tweet0615 = pd.read_csv(path + 'corona_tweets_0615.csv')
tweet0616 = pd.read_csv(path + 'corona_tweets_0616.csv')
tweet0617 = pd.read_csv(path + 'corona_tweets_0617.csv')
tweet0618 = pd.read_csv(path + 'corona_tweets_0618.csv')
tweet0619 = pd.read_csv(path + 'corona_tweets_0619.csv')
tweet0620 = pd.read_csv(path + 'corona_tweets_0620.csv')
tweet0621 = pd.read_csv(path + 'corona_tweets_0621.csv')
tweet0622 = pd.read_csv(path + 'corona_tweets_0622.csv')
tweet0623 = pd.read_csv(path + 'corona_tweets_0623.csv')
tweet0624 = pd.read_csv(path + 'corona_tweets_0624.csv')
tweet0625 = pd.read_csv(path + 'corona_tweets_0625.csv')
tweet0626 = pd.read_csv(path + 'corona_tweets_0626.csv')
tweet0627 = pd.read_csv(path + 'corona_tweets_0627.csv')
tweet0628 = pd.read_csv(path + 'corona_tweets_0628.csv')
tweet0629 = pd.read_csv(path + 'corona_tweets_0629.csv')
tweet0630 = pd.read_csv(path + 'corona_tweets_0630.csv')

'''
Put all the tweets together and remove the duplicated tweets
'''
first_wave_tweets = pd.concat([tweet0320_p1, tweet0320_p2, tweet0320_p3, tweet0321, tweet0322, tweet0323, tweet0324,
                               tweet0325, tweet0326, tweet0327, tweet0328, tweet0330, tweet0331, tweet0401, tweet0402,
                               tweet0403, tweet0404, tweet0405, tweet0406, tweet0407, tweet0408, tweet0409, tweet0410,
                               tweet0411, tweet0412, tweet0413, tweet0414, tweet0415, tweet0416, tweet0417, tweet0418,
                               tweet0419, tweet0420, tweet0421, tweet0422, tweet0423, tweet0424, tweet0425, tweet0426,
                               tweet0427, tweet0428, tweet0429, tweet0430, tweet0501, tweet0502, tweet0503, tweet0504,
                               tweet0505, tweet0506, tweet0507, tweet0508, tweet0509, tweet0510, tweet0511, tweet0512,
                               tweet0513, tweet0514, tweet0515, tweet0516, tweet0517, tweet0518, tweet0519, tweet0520,
                               tweet0521, tweet0522, tweet0523, tweet0524, tweet0525, tweet0526, tweet0527, tweet0528,
                               tweet0529, tweet0530, tweet0531, tweet0601, tweet0602, tweet0603, tweet0604, tweet0605,
                               tweet0606, tweet0607, tweet0608, tweet0609, tweet0610, tweet0611, tweet0612, tweet0613,
                               tweet0614, tweet0615, tweet0616, tweet0617, tweet0618, tweet0619, tweet0620, tweet0621,
                               tweet0622, tweet0623, tweet0624, tweet0625, tweet0626, tweet0627, tweet0628, tweet0629,
                               tweet0630], axis=0, ignore_index=True).drop_duplicates()

print(first_wave_tweets.shape)

'''
Choose the English tweets
'''
first_wave_tweets = first_wave_tweets.loc[first_wave_tweets["lang"] == "en"]
print(first_wave_tweets.shape)
# print(first_wave_tweets)

'''
Reset the index of the tweets
'''
first_wave_tweets = first_wave_tweets.reset_index(drop=True)
# print(first_wave_tweets)

'''
Extract the text of tweets
'''
first_wave_tweets = first_wave_tweets["text"]
# print(first_wave_tweets)

'''
Convert the tweets format to tabular data
'''
first_wave_tweets = pd.DataFrame(first_wave_tweets)
# print(first_wave_tweets)


def cleanTweetsAttribute(text):
    # Removing urls
    text = re.sub(r'http\S+', '', text)  # remove http links
    text = re.sub(r'bit.ly/\S+', '', text)  # remove bitly links
    text = text.strip('[link]')  # remove [links]
    text = text.strip('RT ')  # remove retweet sign 'RT'

    # Removing user mentions
    text = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', text)

    # Removing hashtags
    text = re.sub(r"#(\w+)", '', text, flags=re.MULTILINE)

    return text

def tweetsPreprocessing(text):
    text = cleanTweetsAttribute(text)

    # Converting to lowercase
    text = text.lower()

    # Removing punctuations
    text = text.translate(str.maketrans('', '', string.punctuation))

    return text


def sentiment_analyzer(input_text):
    score = TextBlob(input_text).sentiment.polarity
    return score

first_wave_tweets["text"] = first_wave_tweets["text"].apply(tweetsPreprocessing)
print(first_wave_tweets)

'''
Sentiment analysis of tweets(positive, negative or neutral) by using TextBlob library
TextBlob’s output for a polarity task is a float within the range [-1.0, 1.0]
where -1.0 is a negative polarity and 1.0 is positive. This score can also be equal to 0,
which stands for a neutral evaluation
'''

first_wave_tweets['sentiment'] = first_wave_tweets["text"].apply(sentiment_analyzer)
print(first_wave_tweets)

positive_count = 0
negative_count = 0
neutral_count = 0
output = open("datasets/twitter_sentiment.txt", "w")

for i in first_wave_tweets["sentiment"]:
    if i < 0:
        negative_count += 1
        output.write("neg")
        output.write('\n')
    if i == 0:
        neutral_count += 1
    else:
        positive_count += 1
        output.write("pos")
        output.write('\n')

x = [positive_count, negative_count, neutral_count]
tot = positive_count + negative_count + neutral_count
positive_count_per = round((positive_count / tot) * 100, 1)
negative_count_per = round((negative_count / tot) * 100, 1)
neutral_count_per = 100 - positive_count_per - negative_count_per
print(positive_count_per, negative_count_per, neutral_count_per)

labels = "positive", "negative", "neutral"
sizes = [positive_count_per, negative_count_per, neutral_count_per]
explode = (0, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax.axis("equal")
plt.title('First wave of COVID19')
plt.show()


'''
Trend of public sentiment towards COVID-19
'''
def tweet_sentiment(tweets):
    output = open("datasets/twitter_sentiment.txt", "w")

    for tweet in tweets["text"]:
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence * 100 >= 80:
            output.write(sentiment_value)
            output.write('\n')

    output.close()
    return True

tweet_sentiment(first_wave_tweets)


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    pullData = open("datasets/twitter_sentiment.txt").read()
    lines = pullData.split("\n")

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)

    ax1.clear()
    ax1.plot(xar, yar)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


'''
Word cloud of 50 most frequent words
'''
stopwords = set(stopwords.words('english'))
stopwords.update(["40", "jan", "ppl", "amp", "may"])

cv = CountVectorizer(stop_words = stopwords)
words = cv.fit_transform(first_wave_tweets["text"])

sum_words = words.sum(axis=0)

words_freq = [(word, sum_words[0, i]) for word, i in cv.vocabulary_.items()]
words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)

frequency = pd.DataFrame(words_freq, columns=['word', 'freq'])

frequency.head(50).plot(x='word', y='freq', kind='bar', figsize=(15, 7), color = 'blue')
plt.title("Top 50 most frequently mentioned words")
plt.show()


wordcloud = WordCloud(max_words=50, width=1500, height=1250,
                      background_color="black").generate_from_frequencies(dict(words_freq))

# Display the generated image:
plt.figure(1, figsize=(12, 10))
plt.imshow(wordcloud, interpolation='bilinear')
# plt.imshow(wordcloud)
plt.axis("off")
plt.show()


'''
The trend of the volume of COVID-19-related tweets (first wave)
'''
labels = ["20/3", "21/3", "22/3", "23/3", "24/3", "25/3", "26/3", "27/3", "28/3", "30/3", "31/3",
          "01/4", "02/4", "03/4", "04/4", "05/4", "06/4", "07/4", "08/4", "09/4", "10/4", "11/4",
          "12/4", "13/4", "14/4", "15/4", "16/4", "17/4", "18/4", "19/4", "20/4", "21/4", "22/4",
          "23/4", "24/4", "25/4", "26/4", "27/4", "28/4", "29/4", "30/4", "01/5", "02/5", "03/5",
          "04/5", "05/5", "06/5", "07/5", "08/5", "09/5", "10/5", "11/5", "12/5", "13/5", "14/5",
          "15/5", "16/5", "17/5", "18/5", "19/5", "20/5", "21/5", "22/5", "23/5", "24/5", "25/5",
          "26/5", "27/5", "28/5", "29/5", "30/5", "31/5", "01/6", "02/6", "03/6", "04/6", "05/6",
          "06/6", "07/6", "08/6", "09/6", "10/6", "11/6", "12/6", "13/6", "14/6", "15/6", "16/6",
          "17/6", "18/6", "19/6", "20/6", "21/6", "22/6", "23/6", "24/6", "25/6", "26/6", "27/6",
          "28/6", "29/6", "30/6"]

fig, ax = plt.subplots(1, 1)
plt.xticks(rotation = 60)
tick_spacing = 3
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.bar(labels, tweet_volume, align="center", alpha=1, color="blue")
plt.ylabel('Volume')
plt.xlabel("Date")
plt.title('First wave of COVID19')
plt.show()


'''
Read the daily tweets of the second wave of covid19 (09.15 ~ 12.31)
'''
tweet0915 = pd.read_csv(path2 + 'corona_tweets_0915.csv')
tweet0916 = pd.read_csv(path2 + 'corona_tweets_0916.csv')
tweet0917 = pd.read_csv(path2 + 'corona_tweets_0917.csv')
tweet0918 = pd.read_csv(path2 + 'corona_tweets_0918.csv')
tweet0919 = pd.read_csv(path2 + 'corona_tweets_0919.csv')
tweet0920 = pd.read_csv(path2 + 'corona_tweets_0920.csv')
tweet0921 = pd.read_csv(path2 + 'corona_tweets_0921.csv')
tweet0922 = pd.read_csv(path2 + 'corona_tweets_0922.csv')
tweet0923 = pd.read_csv(path2 + 'corona_tweets_0923.csv')
tweet0924 = pd.read_csv(path2 + 'corona_tweets_0924.csv')
tweet0925 = pd.read_csv(path2 + 'corona_tweets_0925.csv')
tweet0926 = pd.read_csv(path2 + 'corona_tweets_0926.csv')
tweet0927 = pd.read_csv(path2 + 'corona_tweets_0927.csv')
tweet0928 = pd.read_csv(path2 + 'corona_tweets_0928.csv')
tweet0929 = pd.read_csv(path2 + 'corona_tweets_0929.csv')
tweet0930 = pd.read_csv(path2 + 'corona_tweets_0930.csv')
tweet1001 = pd.read_csv(path2 + 'corona_tweets_1001.csv')
tweet1002 = pd.read_csv(path2 + 'corona_tweets_1002.csv')
tweet1003 = pd.read_csv(path2 + 'corona_tweets_1003.csv')
tweet1004 = pd.read_csv(path2 + 'corona_tweets_1004.csv')
tweet1005 = pd.read_csv(path2 + 'corona_tweets_1005.csv')
tweet1006 = pd.read_csv(path2 + 'corona_tweets_1006.csv')
tweet1007 = pd.read_csv(path2 + 'corona_tweets_1007.csv')
tweet1008 = pd.read_csv(path2 + 'corona_tweets_1008.csv')
tweet1009 = pd.read_csv(path2 + 'corona_tweets_1009.csv')
tweet1010 = pd.read_csv(path2 + 'corona_tweets_1010.csv')
tweet1011 = pd.read_csv(path2 + 'corona_tweets_1011.csv')
tweet1012 = pd.read_csv(path2 + 'corona_tweets_1012.csv')
tweet1013 = pd.read_csv(path2 + 'corona_tweets_1013.csv')
tweet1014 = pd.read_csv(path2 + 'corona_tweets_1014.csv')
tweet1015 = pd.read_csv(path2 + 'corona_tweets_1015.csv')
tweet1016 = pd.read_csv(path2 + 'corona_tweets_1016.csv')
tweet1017 = pd.read_csv(path2 + 'corona_tweets_1017.csv')
tweet1018 = pd.read_csv(path2 + 'corona_tweets_1018.csv')
tweet1019 = pd.read_csv(path2 + 'corona_tweets_1019.csv')
tweet1020 = pd.read_csv(path2 + 'corona_tweets_1020.csv')
tweet1021 = pd.read_csv(path2 + 'corona_tweets_1021.csv')
tweet1022 = pd.read_csv(path2 + 'corona_tweets_1022.csv')
tweet1023 = pd.read_csv(path2 + 'corona_tweets_1023.csv')
tweet1024 = pd.read_csv(path2 + 'corona_tweets_1024.csv')
tweet1025 = pd.read_csv(path2 + 'corona_tweets_1025.csv')
tweet1026 = pd.read_csv(path2 + 'corona_tweets_1026.csv')
tweet1027 = pd.read_csv(path2 + 'corona_tweets_1027.csv')
tweet1028 = pd.read_csv(path2 + 'corona_tweets_1028.csv')
tweet1029 = pd.read_csv(path2 + 'corona_tweets_1029.csv')
tweet1030 = pd.read_csv(path2 + 'corona_tweets_1030.csv')
tweet1031 = pd.read_csv(path2 + 'corona_tweets_1031.csv')
tweet1101 = pd.read_csv(path2 + 'corona_tweets_1101.csv')
tweet1102 = pd.read_csv(path2 + 'corona_tweets_1102.csv')
tweet1103 = pd.read_csv(path2 + 'corona_tweets_1103.csv')
tweet1104 = pd.read_csv(path2 + 'corona_tweets_1104.csv')
tweet1105 = pd.read_csv(path2 + 'corona_tweets_1105.csv')
tweet1106 = pd.read_csv(path2 + 'corona_tweets_1106.csv')
tweet1107 = pd.read_csv(path2 + 'corona_tweets_1107.csv')
tweet1108 = pd.read_csv(path2 + 'corona_tweets_1108.csv')
tweet1109 = pd.read_csv(path2 + 'corona_tweets_1109.csv')
tweet1110 = pd.read_csv(path2 + 'corona_tweets_1110.csv')
tweet1111 = pd.read_csv(path2 + 'corona_tweets_1111.csv')
tweet1112 = pd.read_csv(path2 + 'corona_tweets_1112.csv')
tweet1113 = pd.read_csv(path2 + 'corona_tweets_1113.csv')
tweet1114 = pd.read_csv(path2 + 'corona_tweets_1114.csv')
tweet1115 = pd.read_csv(path2 + 'corona_tweets_1115.csv')
tweet1116 = pd.read_csv(path2 + 'corona_tweets_1116.csv')
tweet1117 = pd.read_csv(path2 + 'corona_tweets_1117.csv')
tweet1118 = pd.read_csv(path2 + 'corona_tweets_1118.csv')
tweet1119 = pd.read_csv(path2 + 'corona_tweets_1119.csv')
tweet1120 = pd.read_csv(path2 + 'corona_tweets_1120.csv')
tweet1121 = pd.read_csv(path2 + 'corona_tweets_1121.csv')
tweet1122 = pd.read_csv(path2 + 'corona_tweets_1122.csv')
tweet1123 = pd.read_csv(path2 + 'corona_tweets_1123.csv')
tweet1124 = pd.read_csv(path2 + 'corona_tweets_1124.csv')
tweet1125 = pd.read_csv(path2 + 'corona_tweets_1125.csv')
tweet1126 = pd.read_csv(path2 + 'corona_tweets_1126.csv')
tweet1127 = pd.read_csv(path2 + 'corona_tweets_1127.csv')
tweet1128 = pd.read_csv(path2 + 'corona_tweets_1128.csv')
tweet1129 = pd.read_csv(path2 + 'corona_tweets_1129.csv')
tweet1130 = pd.read_csv(path2 + 'corona_tweets_1130.csv')
tweet1201 = pd.read_csv(path2 + 'corona_tweets_1201.csv')
tweet1202 = pd.read_csv(path2 + 'corona_tweets_1202.csv')
tweet1203 = pd.read_csv(path2 + 'corona_tweets_1203.csv')
tweet1204 = pd.read_csv(path2 + 'corona_tweets_1204.csv')
tweet1205 = pd.read_csv(path2 + 'corona_tweets_1205.csv')
tweet1206 = pd.read_csv(path2 + 'corona_tweets_1206.csv')
tweet1207 = pd.read_csv(path2 + 'corona_tweets_1207.csv')
tweet1208 = pd.read_csv(path2 + 'corona_tweets_1208.csv')
tweet1209 = pd.read_csv(path2 + 'corona_tweets_1209.csv')
tweet1210 = pd.read_csv(path2 + 'corona_tweets_1210.csv')
tweet1211 = pd.read_csv(path2 + 'corona_tweets_1211.csv')
tweet1212 = pd.read_csv(path2 + 'corona_tweets_1212.csv')
tweet1213 = pd.read_csv(path2 + 'corona_tweets_1213.csv')
tweet1214 = pd.read_csv(path2 + 'corona_tweets_1214.csv')
tweet1215 = pd.read_csv(path2 + 'corona_tweets_1215.csv')
tweet1216 = pd.read_csv(path2 + 'corona_tweets_1216.csv')
tweet1217 = pd.read_csv(path2 + 'corona_tweets_1217.csv')
tweet1218 = pd.read_csv(path2 + 'corona_tweets_1218.csv')
tweet1219 = pd.read_csv(path2 + 'corona_tweets_1219.csv')
tweet1220 = pd.read_csv(path2 + 'corona_tweets_1220.csv')
tweet1221 = pd.read_csv(path2 + 'corona_tweets_1221.csv')
tweet1222 = pd.read_csv(path2 + 'corona_tweets_1222.csv')
tweet1223 = pd.read_csv(path2 + 'corona_tweets_1223.csv')
tweet1224 = pd.read_csv(path2 + 'corona_tweets_1224.csv')
tweet1225 = pd.read_csv(path2 + 'corona_tweets_1225.csv')
tweet1226 = pd.read_csv(path2 + 'corona_tweets_1226.csv')
tweet1227 = pd.read_csv(path2 + 'corona_tweets_1227.csv')
tweet1228 = pd.read_csv(path2 + 'corona_tweets_1228.csv')
tweet1229 = pd.read_csv(path2 + 'corona_tweets_1229.csv')
tweet1230 = pd.read_csv(path2 + 'corona_tweets_1230.csv')
tweet1231 = pd.read_csv(path2 + 'corona_tweets_1231.csv')

'''
The trend of the volume of COVID-19-related tweets (second wave)
'''
labels = ["15/9", "16/9", "17/9", "18/9", "19/9", "20/9", "21/9", "22/9", "23/9", "24/9", "25/9",
          "26/9", "27/9", "28/9", "29/9", "30/9", "01/10", "02/10", "03/10", "04/10", "05/10", "06/10",
          "07/10", "08/10", "09/10", "10/10", "11/10", "12/10", "13/10", "14/10", "15/10", "16/10", "17/10",
          "18/10", "19/10", "20/10", "21/10", "22/10", "23/10", "24/10", "25/10", "26/10", "27/10", "28/10",
          "29/10", "30/10", "31/10", "01/11", "02/11", "03/11", "04/11", "05/11", "06/11", "07/11", "08/11",
          "09/11", "10/11", "11/11", "12/11", "13/11", "14/11", "15/11", "16/11", "17/11", "18/11", "19/11",
          "20/11", "21/11", "22/11", "23/11", "24/11", "25/11", "26/11", "27/11", "28/11", "29/11", "30/11",
          "01/12", "02/12", "03/12", "04/12", "05/12", "06/12", "07/12", "08/12", "09/12", "10/12", "11/12",
          "12/12", "13/12", "14/12", "15/12", "16/12", "17/12", "18/12", "19/12", "20/12", "21/12", "22/12",
          "23/12", "24/12", "25/12", "26/12", "27/12", "28/12", "29/12", "30/12", "31/12"]

fig, ax = plt.subplots(1, 1)
plt.xticks(rotation = 60)
tick_spacing = 3
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.bar(labels, tweet_volume, align="center", alpha=1, color="blue")
plt.ylabel('Volume')
plt.xlabel("Date")
plt.title('Second wave of COVID19')
plt.show()

second_wave_tweets = pd.concat([tweet0915, tweet0916, tweet0917, tweet0918, tweet0919, tweet0920, tweet0921, tweet0922,
                                tweet0923, tweet0924, tweet0925, tweet0926, tweet0927, tweet0928, tweet0929, tweet0930,
                                tweet1001, tweet1002, tweet1003, tweet1004, tweet1005, tweet1006, tweet1007, tweet1008,
                                tweet1009, tweet1010, tweet1011, tweet1012, tweet1013, tweet1014, tweet1015, tweet1016,
                                tweet1017, tweet1018, tweet1019, tweet1020, tweet1021, tweet1022, tweet1023, tweet1024,
                                tweet1025, tweet1026, tweet1027, tweet1028, tweet1029, tweet1030, tweet1031, tweet1101,
                                tweet1102, tweet1103, tweet1104, tweet1105, tweet1106, tweet1107, tweet1108, tweet1109,
                                tweet1110, tweet1111, tweet1112, tweet1113, tweet1114, tweet1115, tweet1116, tweet1117,
                                tweet1118, tweet1119, tweet1120, tweet1121, tweet1122, tweet1123, tweet1124, tweet1125,
                                tweet1126, tweet1127, tweet1128, tweet1129, tweet1130, tweet1201, tweet1202, tweet1203,
                                tweet1204, tweet1205, tweet1206, tweet1207, tweet1208, tweet1209, tweet1210, tweet1211,
                                tweet1212, tweet1213, tweet1214, tweet1215, tweet1216, tweet1217, tweet1218, tweet1219,
                                tweet1220, tweet1221, tweet1222, tweet1223, tweet1224, tweet1225, tweet1226, tweet1227,
                                tweet1228, tweet1229, tweet1230, tweet1231], axis=0, ignore_index=True).drop_duplicates()

print(second_wave_tweets.shape)

'''
Choose the English tweets
'''
second_wave_tweets = second_wave_tweets.loc[second_wave_tweets["lang"] == "en"]
print(second_wave_tweets.shape)
# print(second_wave_tweets)

'''
Reset the index of the tweets
'''
second_wave_tweets = second_wave_tweets.reset_index(drop=True)
# print(second_wave_tweets)

'''
Extract the text of tweets
'''
second_wave_tweets = second_wave_tweets["text"]
# print(second_wave_tweets)

'''
Convert the tweets format to tabular data
'''
second_wave_tweets = pd.DataFrame(second_wave_tweets)
# print(second_wave_tweets)

second_wave_tweets["text"] = second_wave_tweets["text"].apply(tweetsPreprocessing)
print(second_wave_tweets)

second_wave_tweets['sentiment'] = second_wave_tweets["text"].apply(sentiment_analyzer)
print(second_wave_tweets)

positive_count = 0
negative_count = 0
neutral_count = 0
output = open("datasets/twitter_sentiment.txt", "w")

for i in second_wave_tweets["sentiment"]:
    if i < 0:
        negative_count += 1
        output.write("neg")
        output.write('\n')
    if i == 0:
        neutral_count += 1
    else:
        positive_count += 1
        output.write("pos")
        output.write('\n')

x = [positive_count, negative_count, neutral_count]
tot = positive_count + negative_count + neutral_count
positive_count_per = round((positive_count / tot) * 100, 1)
negative_count_per = round((negative_count / tot) * 100, 1)
neutral_count_per = 100 - positive_count_per - negative_count_per
print(positive_count_per, negative_count_per, neutral_count_per)


labels = "positive", "negative", "neutral"
sizes = [positive_count_per, negative_count_per, neutral_count_per]
explode = (0, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax.axis("equal")
plt.title('Second wave of COVID19')
plt.show()

'''
Word cloud of 50 most frequent words
'''
stopwords = set(stopwords.words('english'))
stopwords.update(["40", "jan", "ppl", "amp", "may"])

cv = CountVectorizer(stop_words = stopwords)
words = cv.fit_transform(second_wave_tweets["text"])

sum_words = words.sum(axis=0)

words_freq = [(word, sum_words[0, i]) for word, i in cv.vocabulary_.items()]
words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)

frequency = pd.DataFrame(words_freq, columns=['word', 'freq'])

frequency.head(50).plot(x='word', y='freq', kind='bar', figsize=(15, 7), color='blue')
plt.title("Top 50 most frequently mentioned words")
plt.show()


wordcloud = WordCloud(max_words=50, width=1500, height=1250,
                      background_color="black").generate_from_frequencies(dict(words_freq))

# Display the generated image:
plt.figure(1, figsize=(12, 10))
plt.imshow(wordcloud, interpolation='bilinear')
# plt.imshow(wordcloud)
plt.axis("off")
plt.show()
