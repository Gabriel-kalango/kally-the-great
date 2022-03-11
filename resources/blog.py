

from flask_restful import reqparse,Resource
from model.blogmodel import blogostmodel
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
class blogby_id(Resource):
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


