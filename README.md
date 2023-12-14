## <b>AML 3104 Project:</b>
## <b>Model to Predict Client Subscription to Term Deposit</b>

<b>Problem Statement:</b>
- A bank needs to identify customers who are likely to subscribe to Term Deposit. This will help the bank improve its strategies and optimize marketing campaigns by targeting the right customers.

<b>Objectives:</b>
- Identify factors affecting propensity to subscribe to Term Deposit
- Build a predictive model to identify and segment customers based on their likelihood to get the product
- Deploy the application on a cloud platform so that it is accessible to users

<b>Summary:</b>
- The project evaluates and optimizes a marketing campaign dataset to predict customer subscription to a product which is Term Deposit. The dataset includes various features such as age, job type, marital status, education level, and financial information with the target variable being whether a customer subscribed ('yes') or not ('no'). The project uses feature engineering to enhance predictive capabilities of machine learning models. Two models are employed: Decision Tree classifier and Artificial Neural Network (ANN). Both the Decision Tree  and ANN models are evaluated for accuracy, precision, recall, and F1 score.
- The project concludes with a comparative analysis of the Decision Tree and ANN models, emphasizing their strengths and weaknesses in predicting customer subscriptions. The performance of the ANN and decision tree models is nearly identical. But since the decision tree is easier to understand and more straightforward, this will be the final model. This comprehensive approach ensures a thorough understanding of the marketing campaign's effectiveness and facilitates data-driven decision-making for future campaigns.

<b>Methodology:</b>
- Decision Trees: These are powerful models that are easy to understand and interpret. In this model, the decision tree helps identify significant features and their relationships with the target variable (subscription to term deposit). Decision trees are particularly useful for feature importance analysis, and they assist in creating a clear decision-making path based on the dataset's characteristics. The visualization of the decision tree provides transparency in understanding the rules that lead to a positive or negative outcome. This simplicity is advantageous when the interpretability of the model is crucial.
- Artificial Neural Networks (ANN): These are highly flexible and can capture complex relationships within the data. In this model, the ANN's ability to learn intricate patterns and non-linear dependencies between features makes it suitable for scenarios where decision boundaries are complex. ANNs are capable of automatically extracting relevant features and understanding intricate patterns that might be challenging for a decision tree to capture. They offer a higher level of predictive accuracy by modeling intricate relationships between input features and the target variable.
- Combining Decision Tree and ANN: In this project, both models were used in tandem to leverage the interpretability of the decision tree for feature analysis and rule extraction, while benefiting from the ANN's capacity to capture intricate patterns in the data. This hybrid approach allowed for a well-rounded understanding of the underlying factors influencing the subscription to term deposit, providing both transparency and predictive accuracy.

<b>Model Evaluation:</b>
- Classification Accuracy: The model accuracy is 75%, meaning that 75% of instances are correctly classified. The weighted average is 0.75.
- Precision: Precision for positive instances is 0.25, indicating that the model's positive predictions are correct 25% of the time. For negative instances, precision is higher at 0.93. The weighted average precision is 0.85.
- Recall (Sensitivity): Recall for positive instances is 0.57, indicating that the model captures 57% of the actual positive instances. For negative instances, recall is 0.78. The weighted average recall is 0.75.
- F1 Score: The F1 score on the test set is 0.79, providing a balanced measure of precision and recall. The weighted average is 0.79.
In summary, the Decision Tree model exhibits decent performance on the training set, as evidenced by balanced precision, recall, and F1 score. However, on the test set, precision for positive instances is relatively low, suggesting the model's struggle in correctly identifying positive cases. The choice of metrics depends on the specific goals and priorities of the classification problem at hand.

<b>Input Data (17 Variables):</b>
- 1 - age (numeric)
- 2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services")
- 3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
- 4 - education (categorical: "unknown","secondary","primary","tertiary")
- 5 - default: has credit in default? (binary: "yes","no")
- 6 - balance: average yearly balance, in euros (numeric)
- 7 - housing: has housing loan? (binary: "yes","no")
- 8 - loan: has personal loan? (binary: "yes","no")
- 9 - contact: contact communication type (categorical: "unknown","telephone","cellular")
- 10 - day: last contact day of the month (numeric)
- 11 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
- 12 - duration: last contact duration, in seconds (numeric)
- 13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
- 14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
- 15 - previous: number of contacts performed before this campaign and for this client (numeric)
- 16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")
- 17 - y - has the client subscribed a term deposit? (binary: "yes","no")

<b>Data Source:</b>
- Moro,S., Rita,P., and Cortez,P.. (2012). Bank Marketing. UCI Machine Learning Repository. https://doi.org/10.24432/C5K306.

<b>App Link:</b>
- https://bankmarketingcampaign-prod.nn.r.appspot.com/

<b>Task Distribution:</b>
- Data Cleaning - Luz Zapanta (C0879190)
- Data Exploration, Feature Engineering - Keyvan Amini (C0866360)
- Data Modeling Using Decision Tree - Jovi Fez Bartolata (C0869701)
- Data Modeling Using Decision ANN - Maricris Resma (C0872252)
- UI and Cloud Deployment - Jefford Secondes (C0865112)
