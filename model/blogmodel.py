from db import db
class blogostmodel(db.Model): 

    __tablename__="blog"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    content=db.Column(db.String(4000),nullable=False)
    def __init__(self,title,content):
        self.title=title
        self.content=content
        
    
       
    def json(self):
        return {"title":self.title,"content":self.content,"id":'{}'.format(self.id)}
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
    
    

