
# step 1  : build the dockerfile 
docker image build -t sgtaximap_docker .

# step 2 : run the app 
-- http://containertutorials.com/docker-compose/flask-simple-app.html
-- https://medium.com/@ikod/dockerize-simple-python-flask-app-62461efbe58e
docker run -d -p 5000:5000 sgtaximap_docker