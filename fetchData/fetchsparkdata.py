
from pyspark.sql.types import StringType
from pyspark import SQLContext,SparkContext
from pyspark.sql.session import SparkSession
import pyspark
import redis
import os
from django.conf import settings
import datetime
def fetchspark():
   datafolder=settings.CSVFILE
   #r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, db=0,charset="utf-8",decode_responses=True)
   def redisConnect(a,b,c,d,e):

     # step 2: define our connection information for Redis
     # Replaces with your configuration information
     #print(a,"|",b,c,d,e)
     redis_host = "localhost"
     redis_port = 6379
     redis_password = ""
     try:
        value1=""
        value2=""
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, db=0,charset="utf-8",decode_responses=True)
        #r.flushall()
        r.hmset(a,  {"id":a, "brand":b,"colors":c,"dateAdded":d})
        r.zadd("daterelatedID",{a:e})
        value1=a+"::"+c.lower()
        r.zadd("ColorRealatedID",{value1:e}) 
        value2= a+"::"+b
        r.zadd("BrandRealatedID",{value2:e})    
     except Exception as e:
        print(e)
   conf = pyspark.SparkConf()
   conf.set('spark.ui.showConsoleProgress', False)
   sc = SparkContext.getOrCreate(conf)
   sc.setLogLevel("ERROR")
   spark = SparkSession(sc)
   Employee_rdd = spark.read.csv(datafolder,header="true").select("id","brand","colors","dateAdded").distinct()
   for row in Employee_rdd.dropna().rdd.collect():
     dateman = datetime.datetime.strptime(row.dateAdded,'%Y-%m-%dT%H:%M:%SZ')
     millisec = dateman.timestamp() * 1000
     redisConnect(row["id"],row["brand"],row["colors"],row["dateAdded"],int(millisec))