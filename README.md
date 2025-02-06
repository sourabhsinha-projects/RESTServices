Build few Machine Learning REST services using Flask 

Build the docker image:
First make sure docker is running. In Windows run docker desktop. Next...
<path to irisClassPredictor> docker run -p 5000:7000 iris-rf-api

Run docker image:
<path to irisClassPredictor> docker run -p 5000:5000 iris-rf-api

URL (Note: 172.17.0.2 is the virtual URL, can't be used for accessing the API. Instead use below/localhost):  
http://127.0.0.1:5000/apidocs/