# Arctic Monkeys Lyrics Analysis

This project explores the lyrical content of Arctic Monkeys' discography, focusing on the thematic differences between "night" and "day" songs. The analysis includes sentiment analysis, frequency of key terms, and comparisons between various albums.

# Features
Lyrics Analysis: Process and analyze lyrics from Arctic Monkeys' songs.
Sentiment Analysis: Evaluate and compare the sentiment of songs categorized as "night" vs. "day."
Top Words: Identify and visualize the most frequently used words in the lyrics.
Album Sentiment Comparison: Assess and compare the overall sentiment of different albums.

# Data
The analysis uses song lyrics from Arctic Monkeys' discography. The dataset includes:

Name: Song title
Album: Album or single the song appears on
Lyrics: Full lyrics of the song

# Installation
To set up the project, follow these steps:

Clone the Repository:

git clone https://github.com/yourusername/arctic-monkeys-analysis.git

Navigate to the Project Directory:

cd arctic-monkeys-analysis
Install Required Python Packages:

It's recommended to create a virtual environment for the project:

python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Usage

Execute the analysis script:

python3 arctic_monkeys_nightday.py
This script will perform the analysis and output insights into the console.

# View Results:

Results will include sentiment scores, word frequencies, and other key insights. Graphical outputs may be saved to files in the project directory.

# Key Insights
1. Night vs. Day Themes:
Night Songs: The analysis identifies the thematic focus of songs categorized as "night," often reflecting introspective or darker moods. These songs generally feature lyrics that delve into personal struggles, existential themes, or complex emotions.
Day Songs: In contrast, "day" songs tend to be more upbeat or reflective of positive, everyday experiences. The lyrical content often includes themes of optimism, love, or light-heartedness.

2. Top Words and Their Frequencies:
High Frequency Words: Common terms such as "you," "and," "I," and "it" dominate the lyrics, highlighting the central focus on personal relationships and introspection. The prominence of words like "verse" and "chorus" indicates a structural emphasis in the songs.
Thematic Keywords: Words like "your," "me," "when," and "like" suggest a strong focus on personal connections and emotional experiences, aligning with the themes of both "night" and "day" songs.

3. Sentiment Analysis by Album:

Tranquility Base Hotel & Casino: This album exhibits the highest overall positive sentiment, reflecting a more reflective and possibly introspective tone, with a compound sentiment score of 6.29.

Whatever People Say I Am, That’s What I’m Not: The sentiment here is also positive (4.72), indicating a generally upbeat or hopeful tone in the lyrics.

Suck It and See - Single: Shows a notable drop in sentiment (0.9952), suggesting a mix of moods or more nuanced emotional content.

AM and Humbug: These albums display a more negative sentiment (-0.46 and -6.16, respectively), indicating that the lyrics may explore more challenging or somber themes.

4. Sentiment Comparison:

Night Sentiment: Songs categorized as "night" have a lower average sentiment score (3.29) compared to "day" songs, reflecting their often darker or more introspective nature.

Day Sentiment: Songs categorized as "day" exhibit a higher average sentiment score (10.90), highlighting their generally more positive or uplifting content.

5. Patterns and Trends:
Overall Sentiment Trends: The sentiment scores suggest that Arctic Monkeys' lyrics span a wide emotional range, with some albums leaning towards positivity and others exploring darker themes.

Frequency of Themes: The recurrence of certain words and themes provides insight into recurring motifs in the band's music, such as personal relationships, self-reflection, and existential contemplation.
