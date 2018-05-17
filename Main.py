from ReadAndCleanUpData import ReadAndCleanUpData;



filePath = "./airline_tweets.csv";

readAndCleanUpData_obj = ReadAndCleanUpData(filePath);
readAndCleanUpData_obj.ReadCsv();
readAndCleanUpData_obj.RemoveBadGeoData();


