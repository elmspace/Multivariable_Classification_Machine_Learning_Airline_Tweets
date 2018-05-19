"""
	Author: Ashkan Dehghan
	Description:
	The ML (Machine Learning) class contains a series of Machine Learning algorithms
	to perform Multi-Class Classification.
	The constructor will set the Features and Labels, and will format them according to
	current problem.
"""

"""
	Import Libraries
"""
from sklearn.model_selection import train_test_split;
from sklearn import preprocessing;
import matplotlib.pyplot as plt;
from sklearn.metrics import accuracy_score;
from sklearn.tree import DecisionTreeClassifier;
from sklearn.svm import SVC;
from sklearn.neighbors import KNeighborsClassifier;
from sklearn.naive_bayes import GaussianNB;
import pickle;
import os.path;


class ML:

	"""
		Initializing the ML class.
		Note: Since the features in this problem are city names, we will encode them
		into int values.
	"""
	def __init__(self, inputData, input_reTrainIfModelFound=True):
		# Model archive path
		self.ModelArchivePath = "./ML_TrainedModels/";
		# This flag if True will retrain the model, even if there is a saved model
		# in model archive.
		self.reTrainIfModelFound = input_reTrainIfModelFound;

		le = preprocessing.LabelEncoder();
		# Read in the raw features
		self.X = inputData["Nearest City Name"];
		# Read in the raw labels
		self.y = inputData["airline_sentiment"];
		# Encode the features
		self.X = list(le.fit_transform(self.X));
		inputData["Nearest City Name"] = self.X;
		self.X = inputData["Nearest City Name"].to_frame();


	"""
		This method uses sklearn DescisionTreeClassifies to perform the multi class classification.
	"""
	def DecisionTreeClassifier(self):
		trainedModelName = self.ModelArchivePath+"DecisionTreeClassifier_model.p";
		if((os.path.isfile(trainedModelName)==False) or self.reTrainIfModelFound):
			# Setting up the training and test set.
			X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state = 0);
			# Create the model
			model = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train);
			# Use the test features to get the prediction
			predictions = model.predict(X_test);
			# Calculate the accuracy of the model
			accuracy = accuracy_score(y_test, predictions);
			pickle.dump(model,open(trainedModelName,"wb"));
			print accuracy


	"""
		This method uses sklearn SVC to perform the multi class classification.
	"""
	def SupportVectorMachineClassifier(self):
		trainedModelName = self.ModelArchivePath+"SupportVectorMachineClassifier_model.p";
		if((os.path.isfile(trainedModelName)==False) or self.reTrainIfModelFound):
			# Setting up the training and test set.
			X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state = 0);
			# Create the model
			model = SVC(kernel = 'linear', C = 1).fit(X_train, y_train);
			# Calculate the accuracy of the model
			accuracy = model.score(X_test, y_test);
			pickle.dump(model,open(trainedModelName,"wb"));
			print accuracy


	"""
		This method uses sklearn KNeighborsClassifier to perform the multi class classification.
	"""
	def kNearestNeighboursClassifier(self):
		trainedModelName = self.ModelArchivePath+"kNearestNeighboursClassifier_model.p";
		if((os.path.isfile(trainedModelName)==False) or self.reTrainIfModelFound):
			# Setting up the training and test set.
			X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state = 0)
			# Create the model
			model = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train)
			# Calculate the accuracy of the model
			accuracy = model.score(X_test, y_test);
			pickle.dump(model,open(trainedModelName,"wb"));
			print accuracy
		 

	"""
		This method uses sklearn GaussianNB to perform the multi class classification.
	"""
	def NaiveBayesClassifier(self):
		trainedModelName = self.ModelArchivePath+"NaiveBayesClassifier_model.p";
		if((os.path.isfile(trainedModelName)==False) or self.reTrainIfModelFound):
			# Setting up the training and test set.
			X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state = 0)
			# Create the model
			model = GaussianNB().fit(X_train, y_train) 
			# Calculate the accuracy of the model
			accuracy = model.score(X_test, y_test);
			pickle.dump(model,open(trainedModelName,"wb"));
			print accuracy