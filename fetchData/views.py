from django.shortcuts import render

# Create your views here.

import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import datetime
import operator
import collections
#import fetchsparkdata
from . import fetchsparkdata



# Connect to our Redis instance
redisConn = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB,charset="utf-8",decode_responses=True)
redisConn.flushall()
fetchsparkdata.fetchspark()
@api_view(['POST'])
def recent_items(request):
 if request.method =='POST':
        item = json.loads(request.body)#date will  be provided
        key = list(item.keys())[0]
        value = item[key]
        pair={}
        #print(value)
        try:
         if key.lower() !="date":
          raise KeyError
         datetime.datetime.strptime(value, '%Y-%m-%d')
         value1=value+"T00:00:00Z";value2=value+"T23:59:59Z"
         starttime= datetime.datetime.strptime(value1,'%Y-%m-%dT%H:%M:%SZ')
         starttime1 = int(starttime.timestamp() * 1000) ;#print(starttime1)
         endtime= datetime.datetime.strptime(value2,'%Y-%m-%dT%H:%M:%SZ')
         endtime1 = int(endtime.timestamp() * 1000);#print(endtime1,"end")
         Allitems=redisConn.zrangebyscore("daterelatedID", starttime1,endtime1)
         user=Allitems[len(Allitems)-1]
         for key in redisConn.hkeys(user):
            pair[key] = redisConn.hget(user,key)
         
         response = {
            'result':pair
         }
         return Response(response, 200)
        except ValueError:
         #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
         response = {
            'ValueError': "Incorrect data format, should be YYYY-MM-DD"
         }
         return Response(response, 201)
        except KeyError:
         #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
         response = {
            'KeyError': "date must be provided in request"
         }
         return Response(response, 201)
        
 return Response(response, 201)
@api_view(['POST'])
def brand_count(request):
 if request.method =='POST':
        item = json.loads(request.body)#date will  be provided
        key = list(item.keys())[0]
        value = item[key]
        pair={}
        #print(value)
        try:
         if key.lower() !="date":
          raise KeyError
         datetime.datetime.strptime(value, '%Y-%m-%d')
         value1=value+"T00:00:00Z";value2=value+"T23:59:59Z"
         starttime= datetime.datetime.strptime(value1,'%Y-%m-%dT%H:%M:%SZ')
         starttime1 = int(starttime.timestamp() * 1000) ;#print(starttime1)
         endtime= datetime.datetime.strptime(value2,'%Y-%m-%dT%H:%M:%SZ')
         endtime1 = int(endtime.timestamp() * 1000);#print(endtime1,"end")
         Allitems=redisConn.zrangebyscore("BrandRealatedID", starttime1,endtime1)
         #print(Allitems)
         brand=[it.split("::")[1].strip() for it in Allitems]
         count=collections.Counter(brand)
         descend = dict(sorted(count.items(), key=operator.itemgetter(1),reverse=True))
                 
         response = {
            'brandcount':descend
         }
         return Response(response, 200)
        except ValueError:
         #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
         response = {
            'ValueError': "Incorrect data format, should be YYYY-MM-DD"
         }
         return Response(response, 201)
        except KeyError:
         #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
         response = {
            'KeyError': "date must be provided in request"
         }
         return Response(response, 201)
        
 return Response(response, 201)
@api_view(['POST'])
def color_items(request):
 if request.method =='POST':
        item = json.loads(request.body)
        if(request.body==""):
         response = {
            'result':"Null value in body"
         }
         return Response(response, 201)
         #date will  be provided
        key = list(item.keys())[0]
        value = item[key]
        users=[];colorarray=[];count=0
        #print(value)
        try:
         if key.lower() !="color":
          raise KeyError
         colorvalues=redisConn.zrange("ColorRealatedID",0,-1,desc=True)
         
         for line in colorvalues:
           if(line.split("::")[1].__contains__(value.lower()) or line.split("::")[1].__contains__(","+value.lower())):
            users.append(line.split("::")[0])
            count+=1
           if(count==10):
            break;
            
         #print(users)
         for j in users:
          colorpair={}
          for h in redisConn.hkeys(j):
           colorpair[h]=redisConn.hget(j,h)
          colorarray.append(colorpair)
                
         response = {
            'result':colorarray
         }
         return Response(response, 200)
        except ValueError:
         #raise ValueError("Incorrect color format")
         response = {
            'ValueError': "Incorrect color format"
         }
         return Response(response, 201)
        except KeyError:
         #raise ValueError("Incorrect color format")
         response = {
            'KeyError': "color must be provided in request"
         }
         return Response(response, 201)
 response={
   "Error":"Body must be provided for POST operation"
  }  
 return Response(response, 201)

