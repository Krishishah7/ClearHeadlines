# ClearHeadlines: Fake News Articles Detection
"See the truth behind the title!"

# Problem Definition:
In the digital era, fake news spreads faster than facts - often amplified by social media and clickbait headlines. With millions of users consuming news without verifying its authenticity, misinformation can mislead public opinion, damage reputations, and even influence elections. The challenge? Detecting fake news quickly and accurately, especially when users often engage with only the headline.

# Proposed Solution:
To tackle this, ClearHeadlines offers a machine learning-based solution that detects fake news using just the news title.

Here's how:
1. Basic Data Analysis: Combined fake and real news datasets and labeled them as 1 (fake) and 0 (real). Used .head() and .shape() to explore data.
2. Data Preprocessing: Cleaned news titles with tokenization, stopword removal, lemmatization, and regex to remove non-alphabetic characters.
3. Feature Extraction: Applied TF-IDF Vectorization to convert text into numeric features highlighting important words.
4. Model Building: Trained a Passive Aggressive Classifier, suitable for fast and large-scale text classification tasks.
5. Model Evaluation: Assessed performance using accuracy and confusion matrix, achieving 94.18% accuracy in detecting fake news from titles.

# Project Demonstration
![home](https://github.com/user-attachments/assets/1f99ac83-9580-42ec-a5b9-05138b664b73)
![contact](https://github.com/user-attachments/assets/7a720536-33c4-475a-b6f2-001a8952121b)

Dataset Used: [https://drive.google.com/drive/folders/1yUIBIcEVrsd76UR_Ui1Ra8pLTV50EcUy](https://drive.google.com/drive/folders/1yUIBIcEVrsd76UR_Ui1Ra8pLTV50EcUy)


# About Project:
In today’s digital age, the rapid spread of misinformation has become a serious threat to public awareness and trust. With the increasing consumption of news through online platforms and social media, distinguishing between genuine and fake news is more important than ever. This project aims to tackle the issue of fake news by developing a machine learning-based system that can classify news as either genuine or fake based solely on its title.

To achieve this, we have built a predictive model using TF-IDF Vectorization for feature extraction and the Passive Aggressive Classifier algorithm for classification. TF-IDF helps in identifying the most important words in a news title, while the Passive Aggressive Classifier is well-suited for large-scale text classification tasks and performs efficiently in online learning environments.

The model is trained on a labeled dataset of real and fake news titles. After training, it achieved a commendable accuracy of 94.18%, demonstrating its effectiveness in detecting fake news headlines.

This system provides users with a simple interface where they can input a news title and instantly receive a prediction indicating whether the news is likely to be genuine or fake, thereby helping to promote responsible information sharing and media consumption.

# Meet The Developer
Hi, I'm Krishi Shah - the sole developer behind ClearHeadlines. I created this project to fight the spread of misinformation by helping people spot fake news just from the headline.
1. LinkedIn: [krishi-shah-16a934345](https://www.linkedin.com/in/krishi-shah-16a934345/)
2. GitHub: [Krishishah7](https://github.com/Krishishah7/)
