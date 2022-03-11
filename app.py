import os
from flask import Flask
from flask_restful import Api
from resources.blog import Blogpost,blogby_id



uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
api=Api(app)

api.add_resource(Blogpost,"/blog")
api.add_resource(blogby_id,"/blog/<int:_id>")
if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
    