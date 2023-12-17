import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pickle

# Load your dataset
data = pd.read_csv("/opt/airflow/dags/scripts/Weather_Data.csv")

# Drop unnecessary columns
data = data.drop(['Date', 'City', 'Country'], axis=1).dropna()

# Assign binary values based on specific conditions
data['Description_binary'] = data['Description'].isin(['Rain', 'Snow']).astype(int)

# Separate features and target
X = data.drop(['Description', 'Description_binary'], axis=1)
y = data['Description_binary']

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display class distribution before balancing
print("Class distribution before balancing:", Counter(y_train))

# Undersample the majority class using RandomUnderSampler
undersampler = RandomUnderSampler(sampling_strategy='not minority', random_state=42)
X_train_balanced, y_train_balanced = undersampler.fit_resample(X_train, y_train)

# Display class distribution after balancing
print("Class distribution after balancing:", Counter(y_train_balanced))

# Scale numerical features
scaler = StandardScaler()
X_train_balanced_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)


# Train Random Forest on the balanced and scaled dataset
random_forest_model = RandomForestClassifier(n_estimators=40, random_state=42)
random_forest_model.fit(X_train_balanced_scaled, y_train_balanced)

# Evaluate Random Forest model on the test set
y_pred_rf = random_forest_model.predict(X_test_scaled)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred_rf)
precision = precision_score(y_test, y_pred_rf, average='weighted')
recall = recall_score(y_test, y_pred_rf, average='weighted')
f1 = f1_score(y_test, y_pred_rf, average='weighted')
roc_auc = roc_auc_score(y_test, random_forest_model.predict_proba(X_test_scaled)[:, 1])

# Print results
print("Metrics:")
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1 Score: {f1:.2%}")
print(f"AUC-ROC: {roc_auc:.2%}")

# Save the Random Forest model as a pickle file with a new name
new_file_name_rf = '/opt/airflow/dags/scripts/random_forest_model.pkl'
with open(new_file_name_rf, 'wb') as file:
    pickle.dump(random_forest_model, file)
