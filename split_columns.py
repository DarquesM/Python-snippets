import pandas as pd

# Read csv file
# Bad input: only one column, separated with a semicolon
pred = pd.read_csv("pred_3.csv")

# PassengerId;PRED
# 0 	892;0
# 1 	893;0
# 2 	894;0
# 3 	895;0
# 4 	896;0

# Split column on semicolon and fix column names
pred = pd.DataFrame(pred['PassengerId;PRED'].str.split(';').tolist(), columns=['PassengerId', 'Survived'])

#	PassengerId 	Survived
# 0 	892 	0
# 1 	893 	0
# 2 	894 	0
# 3 	895 	0
# 4 	896 	0

# Write file to csv and remove index column
pred.to_csv("solution.csv", index=False)


