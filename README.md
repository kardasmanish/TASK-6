THE OBJECTIVE OF THIS DATA SCIENCE PROJECT IS TO ANALYSE THE TRANSACTIONS AND CLASSIFY THE FRAUD TRANSACTIONS BASED ON THE DATA.


STEP 0 (MEMORY REDUCTION)

- Since the data is huge, memory managment has to be taken care of.
For that reason, a memory reduction feature has been created to reduce the 
memory usage

STEP 1 (EXPLORATORY DATA ANALYSIS)

I will start exploring based on Categorical Features and Transaction Amounts.
The aim is answer some questions like:
- What type of data we have on our data?
- How many cols, rows, missing values we have?
- Whats the target distribution?
- What's the Transactions values distribution of fraud and no fraud transactions?
- We have predominant fraudulent products? 
- What features or target shows some interesting patterns? 
- And a lot of more questions that will raise trought the exploration. 

STEP 2 (FEATURE ENGINEERING AND PCA)

- Creating new features based on the transactions
- Applying PCA algorithm for dimensionality reduction
- Splitting the data into training and test data.

STEP 3 (MODEL BUILDING)

- Selecting the classification algorithm based on stratified K fold cross validation technique.
- Hyperparameter optimization of xgboost using Hyperopt and Optuna

STEP 4 (MODEL EVALUATION)

- The classification model is evaluated on accuracy_score, recall and precision

STEP 5 (EXPLAINABLE AI)

- Using LIME and SHAP for model explainablity
