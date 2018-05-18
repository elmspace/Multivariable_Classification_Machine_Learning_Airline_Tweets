import pickle;
from ReadAndCleanUpData import ReadAndCleanUpData;
from CityDistanceCalculator import ConvertGeoCoordinateToNearestCity;
from ML_Module import *;

# filePath = "./airline_tweets.csv";

# readAndCleanUpData_obj = ReadAndCleanUpData();

# rawData = readAndCleanUpData_obj.Extract(filePath);

# processedData = readAndCleanUpData_obj.Transform(rawData);

# processedData = ConvertGeoCoordinateToNearestCity(processedData);

# pickle.dump(processedData,open("./processedData.p","wb"));


processedData = pickle.load(open("./processedData.p","rb"));


DecisionTreeClassifier(processedData);
SupportVectorMachineClassifier(processedData);
kNearestNeighboursClassifier(processedData);
NaiveBayesClassifier(processedData)