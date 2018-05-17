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
		This constructor will initialized the ReadAndCleanUpData class.
		Input: File path to the raw csv data
	"""
	def __init__(self, input_RawCsvPath):
		self.rawCsvPath = input_RawCsvPath;
		self.rawData = None;
		self.cleansedData = None;


	"""
		This method will read in the raw data from the csv file.
		Input: It takes no input, file path is given in class constructor.
	"""
	def ReadCsv(self):
		try:
			self.rawData = pd.read_csv(self.rawCsvPath);
		except Exception as e:
			raise ValueError("Unable to read raw csv file. Please check the input file. Error: ["+str(e)+"]");
		

	"""
		This method will remove the rows from the raw data which have bad Geo-Coordinates.
		Bad Geo-Coordinate is defined as:
		- None (empty) values
		- Geo-Coordinate = [0.0, 0.0]
	"""
	def RemoveBadGeoData(self):
		try:
			# Make a copy of the raw data.
			if(self.cleansedData == None):
				self.cleansedData = self.rawData.copy(deep=True);
			# Drop rows with empty geo-coordinate. 
			self.cleansedData.dropna(axis=0, subset=['tweet_coord'], inplace=True);
			# Lets also clean up [0.0,0.0] coordinates
			# Extract the coordinate into a list (it is faster working with list then iterating throw DataFrame rows)
			temp_CoordinateList = list(self.cleansedData["tweet_coord"]);
			for i in range(len(temp_CoordinateList)):
				# If the coordinate is [0.0,0.0], set the value to None.
				if(temp_CoordinateList[i] == [0.0,0.0]):
					temp_CoordinateList[i] = None;
			# Set the list back to the column in the DataFrame
			self.cleansedData["tweet_coord"] = temp_CoordinateList;
			# Drop the None values, which were the original [0.0,0.0]
			self.cleansedData.dropna(axis=0, subset=['tweet_coord'], inplace=True);
			# At this point, the data is cleansed.
		except Exception as e:
			raise ValueError("Unable to remove bad geo-coordinate data. Error: ["+str(e)+"]");

