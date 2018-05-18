# importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn import preprocessing;
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score





def DecisionTreeClassifier(inputData):

	le = preprocessing.LabelEncoder();

	# X -> features, y -> label
	X = inputData["Nearest City Name"]
	y = inputData["airline_sentiment"]
	X = list(le.fit_transform(X));
	inputData["Nearest City Name"] = X;
	X = inputData["Nearest City Name"].to_frame();

	# dividing X, y into train and test data
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

	# training a DescisionTreeClassifier
	from sklearn.tree import DecisionTreeClassifier
	dtree_model = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train)
	dtree_predictions = dtree_model.predict(X_test)

	# creating a confusion matrix
	labels = list(set(list(y)));
	accuracy = accuracy_score(y_test, dtree_predictions)
	print accuracy







def SupportVectorMachineClassifier(inputData):
 
	le = preprocessing.LabelEncoder();

	# X -> features, y -> label
	X = inputData["Nearest City Name"]
	y = inputData["airline_sentiment"]
	X = list(le.fit_transform(X));
	inputData["Nearest City Name"] = X;
	X = inputData["Nearest City Name"].to_frame();
 
	# dividing X, y into train and test data
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
	 
	# training a linear SVM classifier
	from sklearn.svm import SVC
	svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
	svm_predictions = svm_model_linear.predict(X_test)
	 
	# model accuracy for X_test  
	accuracy = svm_model_linear.score(X_test, y_test)	 
	print accuracy



def kNearestNeighboursClassifier(inputData):

	le = preprocessing.LabelEncoder();

	# X -> features, y -> label
	X = inputData["Nearest City Name"]
	y = inputData["airline_sentiment"]
	X = list(le.fit_transform(X));
	inputData["Nearest City Name"] = X;
	X = inputData["Nearest City Name"].to_frame();
 
	# dividing X, y into train and test data
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
	 
	# training a KNN classifier
	from sklearn.neighbors import KNeighborsClassifier
	knn = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train)
	 
	# accuracy on X_test
	accuracy = knn.score(X_test, y_test)
	print accuracy
	 



def NaiveBayesClassifier(inputData):
 
	le = preprocessing.LabelEncoder();

	# X -> features, y -> label
	X = inputData["Nearest City Name"]
	y = inputData["airline_sentiment"]
	X = list(le.fit_transform(X));
	inputData["Nearest City Name"] = X;
	X = inputData["Nearest City Name"].to_frame();
	 
	# dividing X, y into train and test data
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
	 
	# training a Naive Bayes classifier
	from sklearn.naive_bayes import GaussianNB
	gnb = GaussianNB().fit(X_train, y_train)
	gnb_predictions = gnb.predict(X_test)
	 
	# accuracy on X_test
	accuracy = gnb.score(X_test, y_test)
	print accuracy