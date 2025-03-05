import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1️⃣ Load phishing dataset (Assuming CSV file with 'text' and 'label' columns)
df = pd.read_csv(r"C:\Users\balac\OneDrive\Documents\Desktop\phishing_extension\phishing_emails.csv")  # Labels: 1 = Phishing, 0 = Safe

# 2️⃣ Convert text into numerical features using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# 3️⃣ Split data into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# 5️⃣ Test model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# 6️⃣ Save the model and vectorizer
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("✅ Model trained and saved successfully!")
