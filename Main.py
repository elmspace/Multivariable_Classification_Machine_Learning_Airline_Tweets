import pickle;
from ReadAndCleanUpData import ReadAndCleanUpData;
from CityDistanceCalculator import ConvertGeoCoordinateToNearestCity;
from ML_Module import ML;
from PredictionModule import PredictionClass;

if(False):
	filePath = "./airline_tweets.csv";
	readAndCleanUpData_obj = ReadAndCleanUpData();
	rawData = readAndCleanUpData_obj.Extract(filePath);
	processedData = readAndCleanUpData_obj.Transform(rawData);
	processedData = ConvertGeoCoordinateToNearestCity(processedData);
	pickle.dump(processedData,open("./processedData.p","wb"));


if(False):
	processedData = pickle.load(open("./processedData.p","rb"));


if(False):
	######################## Use the ML class to train various models
	reTrainIfModelFound = True;
	MLobj = ML(processedData, reTrainIfModelFound);
	MLobj.DecisionTreeClassifier();
	MLobj.SupportVectorMachineClassifier();
	MLobj.kNearestNeighboursClassifier();
	MLobj.NaiveBayesClassifier();
	########################


if(True):
	filePath = "./cities.csv";
	readAndCleanUpData_obj = ReadAndCleanUpData();
	rawData = readAndCleanUpData_obj.Extract(filePath);
	predictionObject = PredictionClass(rawData);
	predictionData = predictionObject.PredictUsingModel("DecisionTreeClassifier_model");