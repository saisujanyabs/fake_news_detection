import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Load data
fake = pd.read_csv('data/Fake.csv')
true = pd.read_csv('data/True.csv')

# Add labels
fake['target'] = 'fake'
true['target'] = 'true'

# Combine data
data = pd.concat([fake, true]).reset_index(drop=True)
data.drop(["date", "title"], axis=1, inplace=True)

# Clean data
data['text'] = data['text'].str.lower()
data['text'] = data['text'].str.replace(r'[^\w\s]', '', regex=True)


# Split data
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['target'], test_size=0.2, random_state=42)

# Create pipeline
model = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('model', MultinomialNB())
])

# Train the model
model.fit(X_train, y_train)

# Function to predict
def predict_news(text):
    prediction = model.predict([text])
    return prediction[0]

