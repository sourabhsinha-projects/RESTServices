""""
    Created on 2019-11-19
    @auther: sourabh sinha
    
    This is the main file for the currentTimeApp which can be called to get the current time 
    or do some time opetations on the current time.
"""
from datetime import datetime, timedelta
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def showCurrentTime():
    
    dDel = request.form["dDel"]
    #mDel = request.form("mDel")   
    #hDel = request.form("hDel")
    mDel = request.args.get("mDel") 
    hDel = request.args.get("hDel") 
    
    now = datetime.now()
    
    # print("Current local date and time :", now.strftime("%Y-%m-%d %H:%M-%S"))
    # print("Expected time:")
    
    #return ("Current loacl date-time:", now.strftime("%Y-%m-%d %H-%M-%D"))
    return (now+timedelta(days=int(dDel), minutes=int(mDel), hours=int(hDel))).strftime("%Y-%m-%d %H-%M-%S")

if __name__ == "__main__":
    # print("Current local date and time : ", showCurrentTime())
    # print("Current local date and time : ", app.run()) ## print does not work here
    app.run(port=7000)
    