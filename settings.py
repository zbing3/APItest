#coding=utf-
import pymongo
import motor
database_ip = "211.157.186.106"
connection = pymongo.MongoClient(database_ip,27017)
db = connection.taotie # 请修改为生产环境的数据库名字

db_async = motor.MotorClient(database_ip,27017).open_sync().taotie
