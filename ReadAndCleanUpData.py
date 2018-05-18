"""
	In this module, we will read the raw data from the csv file.
	We will perform the following cleanup:
	- Remove any row, without valid geo-coordinate
	It will then save the data into a separate file
"""


"""
	Import Libraries:
"""
import pandas as pd;


class ReadAndCleanUpData:


	"""
		This method will read in the raw data from the csv file.
		Input: It takes no input, file path is given in class constructor.
	"""
	def Extract(self, rawCsvPath):
		try:
			rawData = pd.read_csv(rawCsvPath);
			return rawData;
		except Exception as e:
			raise ValueError("Unable to read raw csv file. Please check the input file. Error: ["+str(e)+"]");
		

	"""
		This method will remove the rows from the raw data which have bad Geo-Coordinates.
		Bad Geo-Coordinate is defined as:
		- None (empty) values
		- Geo-Coordinate = [0.0, 0.0]
	"""
	def Transform(self, inputRawData):
		try:
			# Make a copy of the raw data.
			processedData = inputRawData.copy(deep=True);
			# Drop rows with empty geo-coordinate. 
			processedData.dropna(axis=0, subset=['tweet_coord'], inplace=True);
			# Lets also clean up [0.0,0.0] coordinates
			# Extract the coordinate into a list (it is faster working with list then iterating throw DataFrame rows)
			temp_CoordinateList = list(processedData["tweet_coord"]);
			for i in range(len(temp_CoordinateList)):
				# If the coordinate is [0.0,0.0], set the value to None.
				if(temp_CoordinateList[i] == [0.0,0.0]):
					temp_CoordinateList[i] = None;
			# Set the list back to the column in the DataFrame
			processedData["tweet_coord"] = temp_CoordinateList;
			# Drop the None values, which were the original [0.0,0.0]
			processedData.dropna(axis=0, subset=['tweet_coord'], inplace=True);
			
			# Filter the data into columns which we need
			processedData = processedData[["airline_sentiment","tweet_coord"]].copy(deep=True);
			# Transform the data, map the sentiment data into ints
			TransformMap = {"negative":0,"neutral":1,"positive":2};
			processedData["airline_sentiment"] = processedData["airline_sentiment"].map(TransformMap);

			tweetCoordList = list(processedData['tweet_coord']);
			tempList = [];
			for coords in tweetCoordList:
				temp = coords;
				temp = temp.replace("[","").replace("]","");
				temp = [float(i) for i in temp.split(",")];
				tempList.append(temp);
			
			processedData['tweet_coord'] = tempList;

			return processedData;
		except Exception as e:
			raise ValueError("Unable to remove bad geo-coordinate data. Error: ["+str(e)+"]");


