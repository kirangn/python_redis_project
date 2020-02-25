"# python_redis_project" 

Abstract:
Design and implement a distributed worker system to update data in Redis using Python.


Data:
For this task, use the dataset given which is based on women's shoe catalog. (https://www.kaggle.com/datafiniti/womens-shoes-prices/)
The dataset contains, "id, brand, colors, dateAdded" as headers. Please assume "id" to be unique. Also ignore records which has null values in any of the columns.


Problem Statement:
There are two parts to this:
1. Database:
You have to use a Redis server to store each of the record, You are free to choose any data structure of redis that will suit the requirements.

2. Spark:
You must use spark dataframes to read the csv dataset, transform it and must insert data into redis parallely, Only the required data for the three REST APIs to function must be stored in redis.


Requirement:
Implement 3 APIs(Restful) to query and fetch data from redis, All requests and responses should be in JSON format.

/getRecentItem - return the most recent item added on the given date
Example:
Input:
2017-02-03
Output:
id: AVpe__eOilAPnD_xSt-H
brand: Fashion Focus
color: yellow

/getBrandsCount - return the count of each brands added on the given date in descending order
Example:
Input:
2017-02-03
Output:
+-----------------+-----+
| brand|count|
+-----------------+-----+
|Personal Identity| 4341|
| Mo Mo| 744|
| Donald J Pliner| 281|
| Gola| 52|
| Gubize| 20|
| Naot| 10|
| Fashion Focus| 6|
| Electric Karma| 5|
| Evan Picone| 2|
| Ros Hommerson| 1|
| Patrizia| 1|
............... ...
............... ...
............... ...
+-----------------+-----+


/getItemsbyColor - return the top 10 latest items given input as color
Example:
Input:
Blue
Output:
[{
id: AVpe__eOilAPnD_xSt-H
brand: Fashion Focus
color: yellow
date: 2016-11-11T09:50:34Z|
},
....
....
]




#HOW_TO_RUN

step1:clone the given repository https://github.com/kirangn/python_redis_project.git

step2:Download the files to the local machine 

step3:Download dataset from the given link https://www.kaggle.com/datafiniti/womens-shoes-prices/

step4:Make sure you change CSVFILE  path in settings.py file to the path where dataset folder is present

step5:Make sure all the dependencies are been installed (Provided below)

step6: run the command "python <folderpath of download files>\manage.py runserver" 

step7:Once the server is started run the following urls http://127.0.0.1:8000/fetchData/getItemsbyColor ,http://127.0.0.1:8000/fetchData/getBrandsCount, http://127.0.0.1:8000/fetchData/getRecentItem in web browser or postman. Use the POST Method and give the key:pair data in the body.

#DEPENDENCIES:

java installed on machine jdk 8 
ApacheSpark ==spark-2.4.5-bin-hadoop2.7
python > 3 and its dependencies:
	asgiref==3.2.3
	Django==3.0.3
	djangorestframework==3.11.0
	findspark==1.3.0
	numpy==1.18.1
	pandas==1.0.1
	py4j==0.10.7
	pyspark==2.4.5
	python-dateutil==2.8.1
	pytz==2019.3
	redis==3.4.1
	six==1.14.0
	sqlparse==0.3.0
Redis server==3.0


All Dependencies are been installed using the command pip install -r requirements.txt



