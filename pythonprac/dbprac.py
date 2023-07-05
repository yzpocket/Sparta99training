from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://ohnyong:test@cluster0.lu7mz8j.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

# Dictionary 선언
# doc = {
#     'name':'영수',
#     'age':24
# }

# insert문
# db.users.insert_one(doc)


#------------ CRUD SQL --------------#
# INSERT_ONE
# 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

# READ(FIND_ONE)
# 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
# print(user)

# READ(FIND)
# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))
# for a in all_users:
#     print(a)

# UPDATE
# 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# DELETE
# 지우기 - 예시
db.users.delete_one({'name':'bobby'})