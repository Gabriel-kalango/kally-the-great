
from flask import Flask, session
from flask_restful import Resource,Api,reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
db=SQLAlchemy()

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
api=Api(app)
@app.before_first_request
def create_table():
    db.create_all()
class Blogpost(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("title",
    type=str,
    required=True,
    help="this field cannot be left blank")


    
    parser.add_argument("content",
    type=str,
    required=True,
    help="this field cannot be left blank")
    
    
   

    def post(self):
        data=Blogpost.parser.parse_args()
        item=blogostmodel.findbytitle(data["title"]) 
        if item:
            return {"message":"this post already exist"}
        
        data=Blogpost.parser.parse_args()
        user=blogostmodel( **data)
        blogostmodel.save_to_db(user)
        return {"message":"created"},201
    def get(self):
        
      
        return {"blog":[x.json() for x in blogostmodel.query.all()]}
class delete(Resource):
    def delete(self,_id):
        item=blogostmodel.findbyid(_id)
        if item:
            blogostmodel.delete_from_db(item),200
            
        else:
            return {"message":"the post with this id doesnt exist "},400
        return {"message":"post has been deleted"},200

        
    def put(self,_id):
        data=Blogpost.parser.parse_args()
        item=blogostmodel.findbyid(_id)
       
        if item is None:
            return {"message":"post not found"}

        else:
            if data["title"]:
                item.title=data["title"]
            if data["content"]:
                item.content=data["content" ]
            item.save_to_db()
        return {"message":"update is complete"},200



class blogostmodel(db.Model): 
    __tablename__="blog"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=false)
    content=db.Column(db.String(4000),nullable=False)
    def __init__(self,title,content):
        self.title=title
        self.content=content
        
    
       
    def json(self):
        return {"title":self.title,"content":self.content,"id":'<id {}>'.format(self.id)}
    def save_to_db(self):

       db.session.add(self)
       db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def findbyid(cls,_id):
        return cls.query.filter_by(id=_id).first()
    @classmethod
    def findbytitle(cls,title):
        return cls.query.filter_by(title=title).first()
    
    


api.add_resource(Blogpost,"/blog")
api.add_resource(delete,"/blog/<int:_id>")
if __name__=="__main__":
    db.init_app(app)
    app.run(debug=True)
    