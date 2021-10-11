

* Go to the project directory
* Build your FastAPI image:
> docker build -t myimage .
* Run a container based on your image:
> docker run -d --name mycontainer -p 80:80 myimage

Now you can go to http://192.168.99.100/docs or http://127.0.0.1/docs (or equivalent, using your Docker host).\
You will see the automatic interactive API documentation (provided by Swagger UI)

And you can also go to http://192.168.99.100/redoc or http://127.0.0.1/redoc (or equivalent, using your Docker host).\
You will see the alternative automatic documentation (provided by ReDoc)