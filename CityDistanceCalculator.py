"""
	Author: Ashkan Dehghan

	Description: This module contains functions to read in the city csv file,
	and convert coordinates to nearest city using Euclidean distance. 
"""

"""
	Import libraries
"""
import pandas as pd;
import math;


pathToCitiesCsvFile = "./cities.csv";


def ConvertGeoCoordinateToNearestCity(input_AirlineDataFrame):
	# Lets read in the cities csv
	citiesData = pd.read_csv(pathToCitiesCsvFile);
	# Get the cities name, lat and lng, into list
	cities_Name = citiesData["asciiname"];
	cities_Lat = citiesData["latitude"];
	cities_Lng = citiesData["longitude"];

	# Also get the lat/lng from airline tweets
	airlineTweet_LatLng = input_AirlineDataFrame["tweet_coord"];

	airlineTweet_ClosestCity_Name = [];
	airlineTweet_ClosestCity_Name = [];
	airlineTweet_ClosestCity_Distance = [];
	for a_LatLng in airlineTweet_LatLng:
		currentDistance = None;
		currentCityName = None;

		lat_temp = [(a_LatLng[0] - i)**2 for i in cities_Lat];
		lng_temp = [(a_LatLng[1] - i)**2 for i in cities_Lng];
		distance = [math.sqrt(lat_temp[i]+lng_temp[i]) for i in range(len(lat_temp))];

		airlineTweet_ClosestCity_Name.append(cities_Name[distance.index(min(distance))]);
		airlineTweet_ClosestCity_Distance.append(min(distance));

	input_AirlineDataFrame["Nearest City Name"] = airlineTweet_ClosestCity_Name;
	input_AirlineDataFrame["Nearest City Distance"] = airlineTweet_ClosestCity_Distance;

	return input_AirlineDataFrame;	



