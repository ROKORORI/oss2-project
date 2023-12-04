import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


# 2-2-1
def sort_dataset(dataset_df):
	sort_data = dataset_df.sort_values(by=['year'], ascending=True)
	return sort_data


# 2-2-2
def split_dataset(dataset_df):
	# salary = label, 0.001 multiply
	# [:1718] = train, [1718:] = test
	split_data = dataset_df
	split_data['salary'] = split_data['salary'] * 0.001

	len_row = len(split_data)
	train = split_data.head(1718)
	test = split_data.tail(len_row - 1718)

	x_train = train
	x_test = test
	y_train = train.loc[:, 'salary']
	y_test = test.loc[:, 'salary']
	return x_train, x_test, y_train, y_test


# 2-2-3
def extract_numerical_cols(dataset_df):
	# 'age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR'
	# 'RBI', 'SB', 'CS', 'BB', 'HBP','SO', 'GDP', 'fly', 'war'
	# 추출
	extract_data = dataset_df.loc[:, ['age', 'G', 'PA', 'AB', 'R',
									'H', '2B', '3B', 'HR', 'RBI',
									'SB', 'CS', 'BB', 'HBP', 'SO',
									'GDP', 'fly', 'war']]
	return extract_data


# 2-2-4
def train_predict_decision_tree(X_train, Y_train, X_test):
	# train & return predict
	dtr_cls = DecisionTreeRegressor()
	dtr_cls.fit(X_train, Y_train)
	predic = dtr_cls.predict(X_test)
	return predic


# 2-2-5
def train_predict_random_forest(X_train, Y_train, X_test):
	# train & return predict
	rfr_cls = RandomForestRegressor()
	rfr_cls.fit(X_train, Y_train)
	predic = rfr_cls.predict(X_test)
	return predic


# 2-2-6
def train_predict_svm(X_train, Y_train, X_test):
	# train & return predict
	svm_pipe = make_pipeline(
		StandardScaler(),
		SVR()
	)
	svm_pipe.fit(X_train, Y_train)
	predic = svm_pipe.predict(X_test)
	return predic


# 2-2-7
def calculate_RMSE(labels, predictions):
	return np.sqrt(np.mean((predictions - labels) ** 2))


if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)

	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)

	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))