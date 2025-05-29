from flask import Flask
from Housing.logger import logging
from Housing.exception import housing_exp
import os, sys


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:       
       housing =  housing_exp(e,sys)
       logging.info(housing.error_message)
    logging.info("We are testing logging module")
    return "My First Machine learning projecct"


if __name__ == '__main__':
    app.run(debug=True)
    