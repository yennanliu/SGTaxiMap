# step 1  : build the dockerfile 
docker image build -t sgtaximap_docker .



# step 2 : run the app 
docker run -d -p 5000:9000 sgtaximap_docker