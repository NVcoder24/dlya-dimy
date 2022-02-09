import os
os.system("pip3 install flask")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Это личный сайт Димы! Реально!</h1><a href='https://www.dns-shop.ru/'>Купи себе уже комп!</a>"

app.run(port=8080)
