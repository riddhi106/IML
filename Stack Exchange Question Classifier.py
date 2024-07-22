import json
import sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer

if sys.version_info[0] >= 3:
    raw_input = input

# Initialize the HashingVectorizer
transformer = HashingVectorizer(stop_words='english')

# Prepare training data
train_data = []
train_labels = []

# Read the training data
with open('training.json') as f:
    num_train = int(f.readline().strip())
    for _ in range(num_train):
        h = json.loads(f.readline().strip())
        train_data.append(h['question'] + "\n" + h['excerpt'])  # Combine question and excerpt
        train_labels.append(h['topic'])

# Transform the training data
train_features = transformer.fit_transform(train_data)

# Train the LinearSVC model
svm = LinearSVC()
svm.fit(train_features, train_labels)

# Prepare test data
test_data = []
num_test = int(raw_input().strip())
for _ in range(num_test):
    h = json.loads(raw_input().strip())
    test_data.append(h['question'] + "\n" + h['excerpt'])  # Combine question and excerpt

# Transform the test data
test_features = transformer.transform(test_data)

# Predict the topics for the test data
test_labels = svm.predict(test_features)

# Output the predictions
for label in test_labels:
    print(label)
