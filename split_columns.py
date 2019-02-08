import pandas as pd

# Read csv file
# Bad input: only one column, separated with a semicolon
pred = pd.read_csv("pred_3.csv")

# Split column on semicolon and fix column names
pred = pd.DataFrame(pred['PassengerId;PRED'].str.split(';').tolist(), columns=['PassengerId', 'Survived'])
# Write file to csv and remove index column
pred.to_csv("solution.csv", index=False)
