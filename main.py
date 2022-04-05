# 1 davaleba
# import sqlite3
#
# connection = sqlite3.connect ('morty.db')
# cursor = connection.cursor()
# cursor.execute("drop table if exists dogs")
# cursor.execute("create table if not exists dogs(name text not null,age integer not null,color text not null")
# cursor.execute("insert into dogs values('jeka,1,black')")
# cursor.execute("insert into dogs values('rox,8,brown')")
# cursor.execute("insert into dogs values('max,4,white')")
# cursor.execute("insert into dogs values('bubu,7,red')")
# cursor.execute("insert into dogs values('rose,0,orange')")
# connection.commit()
# print(cursor.execute("select * from dogs ")).fetchall()
#
#2 davaleba
# class Fruit:
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#
#     def __add__(self, other):
#         return self.weight + other.weight
#     def __eq__(self, other):
#         return self.name == other.name
#
#
# first_person =Fruit('nika', 60)
# second_person=Fruit("nini",46)
# third_person=Fruit('giorgi',90)
# fourth_person=Fruit('aleko',78)
#
# print(first_person+second_person)
# print(third_person+fourth_person)
# print(first_person==fourth_person)
# print(first_person==third_person)





