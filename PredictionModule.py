

"""
	Import Libraries
"""
from sklearn import preprocessing;
import pickle;
import pandas as pd;

class PredictionClass:

	"""
		Initializing the Prediction Class.
		- Input: New data we want to predict on <DataFrame>
	"""
	def __init__(self, inputData):
		# Model archive path
		self.ModelArchivePath = "./ML_TrainedModels/";
		# We need to Encode the data before prediction.
		le = preprocessing.LabelEncoder();
		# Read in the raw features
		self.newData = inputData["asciiname"];
		# Encode the features
		self.newData = list(le.fit_transform(self.newData));
		inputData["asciiname_encoded"] = self.newData;
		self.newData = inputData["asciiname_encoded"].to_frame();
		# Create a results set.
		self.PredictionResults = pd.DataFrame(columns=["City Name","Sentiment Prediction","Sentiment Prediction Probablity"]);		
		self.PredictionResults["City Name"] = list(inputData["asciiname"]);


	"""
		This method will:
		- Load the ML model
		- Run it on the data
		- Get prediction and prediction probability
		- Return the DataFrame with input data and the prediction
		Input: Model Name <str>
		Output: Prediction <Pandas DataFrame>
	"""
	def PredictUsingModel(self, input_ModelName):
		# Load the model from the trained models directory.
		model = pickle.load(open(self.ModelArchivePath+input_ModelName+".p","rb"));
		# Get the prediction from model
		predictions = model.predict(self.newData);
		# Calculate the prediction probability
		predictions_probability = model.predict_proba(self.newData);
		self.PredictionResults["Sentiment Prediction"] = list(predictions);
		self.PredictionResults["Sentiment Prediction Probablity"] = list(predictions_probability);
		return self.PredictionResults;



