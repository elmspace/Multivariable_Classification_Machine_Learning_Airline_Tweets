"""
	External Libraries
"""
import luigi;
import pandas as pd;

base_raw_data = "./raw_data/";
base_clean_data = "./clean_data/";
base_processed_data = "./processed_data/";
base_ml_models = "./ml_models/";
base_prediction_data = "./prediction_data/";



###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
class CleanDataTask(luigi.Task):

	tweet_file = luigi.Parameter()
	output_file = luigi.Parameter(default='clean_data.csv')

	"""
		The first process does not have any requirements.
	"""
	def requires(self):
		return [];


	def output(self):
		return luigi.LocalTarget(base_clean_data+self.output_file);


	"""
		This is the core of the CleanDataTaks. This will run when performing the CleanDataTaks.
	"""
	def run(self):
		# Read the raw data
		rawData = pd.read_csv(base_raw_data+self.tweet_file);
		# Drop rows with empty geo-coordinate.
		rawData.dropna(axis=0, subset=['tweet_coord'], inplace=True);
		# Lets also clean up [0.0,0.0] coordinates
		# Extract the coordinate into a list (it is faster working with list then iterating throw DataFrame rows)
		temp_CoordinateList = list(rawData["tweet_coord"]);
		for i in range(len(temp_CoordinateList)):
			# If the coordinate is [0.0,0.0], set the value to None.
			if(temp_CoordinateList[i] == [0.0,0.0]):
				temp_CoordinateList[i] = None;
		# Set the list back to the column in the DataFrame
		rawData["tweet_coord"] = temp_CoordinateList;
		# Drop the None values, which were the original [0.0,0.0]
		rawData.dropna(axis=0, subset=['tweet_coord'], inplace=True);
		# Get the output file and write the clean data to it
		file = self.output().open("w");
		rawData.to_csv(file);
		file.close();

###############################################################################################################################
###############################################################################################################################
###############################################################################################################################






class TrainingDataTask(luigi.Task):
	""" Extracts features/outcome variable in preparation for training a model.

		Output file should have columns corresponding to the training data:
		- y = airline_sentiment (coded as 0=negative, 1=neutral, 2=positive)
		- X = a one-hot coded column for each city in "cities.csv"
	"""
	tweet_file = luigi.Parameter()
	cities_file = luigi.Parameter(default='cities.csv')
	output_file = luigi.Parameter(default='features.csv')

	
	def output(self):
		return luigi.LocalTarget(base_processed_data+self.output_file);

	"""
		The first process does not have any requirements.
	"""
	def requires(self):
		return [CleanDataTask()];

	def run(self):
		# Read the clean data from previous process
		cleanData = pd.read_csv(self.input());
		













# class TrainModelTask(luigi.Task):
# 	""" Trains a classifier to predict negative, neutral, positive
# 		based only on the input city.

# 		Output file should be the pickle'd model.
# 	"""
# 	tweet_file = luigi.Parameter()
# 	output_file = luigi.Parameter(default='model.pkl')

# 	# TODO...


# class ScoreTask(luigi.Task):
# 	""" Uses the scored model to compute the sentiment for each city.

# 		Output file should be a four column CSV with columns:
# 		- city name
# 		- negative probability
# 		- neutral probability
# 		- positive probability
# 	"""
# 	tweet_file = luigi.Parameter()
# 	output_file = luigi.Parameter(default='scores.csv')

# 	# TODO...


if __name__ == "__main__":
	luigi.run()
