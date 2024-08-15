import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import collections
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the dataset
lyrics = pd.read_csv('arctic_monkeys_lyrics.csv')

# Fill missing values in 'album' column with a placeholder
lyrics['album'] = lyrics['album'].fillna('Unknown Album')

# Update the function to handle more cases
def album_release(row):  
    album = row['album'].lower()
    if 'whatever people say i am' in album:
        return '2006'
    elif 'favourite worst nightmare' in album:
        return '2007'
    elif 'humbug' in album:
        return '2009'
    elif 'suck it and see' in album:
        return '2011'
    elif 'am' in album:
        return '2013'
    elif 'tranquility base hotel & casino' in album:
        return '2018'
    else:
        return 'No Date'

# Apply the updated function
lyrics['album_year'] = lyrics.apply(lambda row: album_release(row), axis=1)

# Remove rows where album_year is 'No Date'
lyrics = lyrics[lyrics['album_year'] != 'No Date']

# Clean the lyric text
lyrics['clean_lyric'] = lyrics['lyrics'].str.lower()
lyrics['clean_lyric'] = lyrics['clean_lyric'].str.replace('[^\w\s]', '', regex=True)
stop = ['the', 'a', 'this', 'that', 'to', 'is', 'am', 'was', 'were', 'be', 'being', 'been']
lyrics['clean_lyric'] = lyrics['clean_lyric'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))

# Define keywords for night and day
night_keywords = ['night', 'midnight', 'dawn', 'dusk', 'evening', 'late', 'dark', '1am', '2am', '3am', '4am']
day_keywords = ['day', 'morning', 'light', 'sun', 'dawn', 'noon', 'golden', 'bright']

# Create columns for night, day keywords
night_regex = '|'.join(night_keywords)
day_regex = '|'.join(day_keywords)
lyrics['night'] = lyrics['clean_lyric'].str.contains(night_regex)
lyrics['day'] = lyrics['clean_lyric'].str.contains(day_regex)

# Count occurrences
night_count = sum(lyrics['night'])
day_count = sum(lyrics['day'])
print(f"Night words: {night_count}")
print(f"Day words: {day_count}")

# Visualize mentions over time
yearly_mentions = lyrics.groupby('album_year').sum().reset_index()

# Plot night and day mentions over years
plt.figure(figsize=(14, 6))
plt.plot(yearly_mentions['album_year'], yearly_mentions['night'], label='Night Mentions', marker='o')
plt.plot(yearly_mentions['album_year'], yearly_mentions['day'], label='Day Mentions', marker='o')
plt.xlabel('Year')
plt.ylabel('Mentions')
plt.title('Night and Day Mentions in Arctic Monkeys Lyrics Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Tokenize the lyrics
lyrics['lyrics_tok'] = lyrics['clean_lyric'].apply(lambda x: word_tokenize(x))

# Count word frequencies
word_list = [word for sublist in lyrics['lyrics_tok'] for word in sublist]
word_frequency = collections.Counter(word_list)
word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
print("Top words and their frequencies:")
for word, freq in word_frequency[:20]:  # Print top 20 words
    print(f"{word}: {freq}")

# Analyze sentiment
sia = SentimentIntensityAnalyzer()
lyrics['polarity'] = lyrics['clean_lyric'].apply(lambda x: sia.polarity_scores(x))
lyrics[['neg', 'neu', 'pos', 'compound']] = lyrics['polarity'].apply(pd.Series)
lyrics.drop('polarity', axis=1, inplace=True)

# Calculate overall sentiment
pos = sum(lyrics['pos'])
neg = sum(lyrics['neg'])
compound = sum(lyrics['compound'])
print(f"Overall Positive Sentiment: {pos}")
print(f"Overall Negative Sentiment: {neg}")
print(f"Overall Compound Sentiment: {compound}")

# Sentiment per album
album_sentiment = lyrics.groupby('album')['compound'].sum().reset_index()
print("Sentiment per album:")
print(album_sentiment.sort_values(by='compound', ascending=False))

# Visualize sentiment over time
yearly_sentiment = lyrics.groupby('album_year').sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(yearly_sentiment['album_year'], yearly_sentiment['compound'], label='Overall Sentiment', marker='o')
plt.xlabel('Year')
plt.ylabel('Sentiment')
plt.title('Overall Sentiment of Arctic Monkeys Lyrics Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Compare sentiment for day vs. night
night_lyrics = lyrics[lyrics['night'] == True]
day_lyrics = lyrics[lyrics['day'] == True]

night_sentiment = night_lyrics['compound'].sum()
day_sentiment = day_lyrics['compound'].sum()

print(f"Night sentiment: {night_sentiment}")
print(f"Day sentiment: {day_sentiment}")
