# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

# Load in training data
fname = 'trainingdata.txt'

targets = []
data = []

with open(fname) as f:
    for line in f:
        targets.append(line[0])
        data.append(line[2:])

# Train the classifier
textClf = Pipeline([
    ('vect', CountVectorizer(max_df=0.5)),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier()),
])
textClf.fit(data, targets)

# Load in test data
docs = []
n = int(input())
for _ in range(n):
    docs.append(input().strip())

# Predict
predicted = textClf.predict(docs)

# Output in hackerrank format
for pred in predicted:
    print(pred)
