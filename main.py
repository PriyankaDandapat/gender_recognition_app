from flask import Flask
from app import veiws

app=Flask(__name__)   #webserver gateway interphase (WSGI)

app.add_url_rule(rule='/',endpoint='home',view_func=veiws.index)
app.add_url_rule(rule='/app/',endpoint='app',view_func=veiws.app)
app.add_url_rule(rule='/app/gender/',endpoint='gender',view_func=veiws.genderapp, methods=['GET','POST'])
