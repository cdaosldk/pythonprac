from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.84m7k3d.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
"""
#가버나움의 평점과 같은 평점의 영화 찾기
target_movie = db.movies.find_one({'title':'가버나움'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    print(movie['title'])

    
db.movies.update_one({'title':'가버나움'},{'$set':{'star':"0"}})
"""
