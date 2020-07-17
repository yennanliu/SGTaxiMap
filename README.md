## SG taxi heatmap 

[![Build Status](https://travis-ci.org/yennanliu/Xjob.svg?branch=master)](https://travis-ci.org/yennanliu/SGTaxiMap)
[![PRs](https://img.shields.io/badge/PRs-welcome-6574cd.svg)](https://github.com/yennanliu/SGTaxiMap/pulls)

### Deploy to Heroku 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yennanliu/SGTaxiMap)

### LIVE VIEW 
[LIVE VIEW](http://sgtaxi-heroku-app.herokuapp.com/)

### DEMO 
demo :  
		![image](https://github.com/yennanliu/SGTaxiMap/blob/master/doc/taxi_location.png)
		![image](https://github.com/yennanliu/SGTaxiMap/blob/master/doc/heatmap.png)

## Quick start 
<details>
<summary>Quick-Start</summary>

### Run (Manually)

```bash
# STEP 1)
# get repo 
$ git clone https://github.com/yennanliu/SGTaxiMap
$ cd && cd SGTaxiMap
# STEP 2)
$ python run.py
# access the app via browser 
# visit http://127.0.0.1:5000 
```

### Run (docker)
```bash
docker run -d -p 5000:5000 yennanliu/sgtaximap_docker:v1
```
### Build
```bash
# https://github.com/yennanliu/SGTaxiMap/blob/master/docker_start.md
$ cd && git clone https://github.com/yennanliu/SGTaxiMap.git && cd SGTaxiMap
$ docker image build -t sgtaximap_docker .
$ docker run -d -p 5000:5000 sgtaximap_docker
```

### Run ETL job  (taxi data collect) :

```bash 
# can modify cron job in /crontab.txt 
# collected data can either saved as csv or DB 
$ /anaconda/envs/<your_dev_env>/bin/python etl/job_luigi.py   Agg_taxi_locations

```

### Run test 
```bash
$ export PYTHONPATH=$(pwd)
$ pytest -v tests/

```
</details>

## Reference 
<details>
<summary>Reference</summary>
- Open source projct 
	- https://github.com/JTLX/SGTaxiHeatMap/blob/master/update_heat.py
	- https://data.gov.sg/developer
	- https://data.gov.sg/api/1/util/snippet/api_info.html?resource_id=31ca0cee-6d9e-453a-8b4f-376d37713a10&datastore_root_url=https%3A%2F%2Fdata.gov.sg%2Fapi%2Faction
	- http://harrywood.co.uk/maps/examples/leaflet/marker-array.view.html

- Automated heat map 
	- http://rmaps.github.io/blog/posts/animated-choropleths/index.html
</details>

## TODO 
<details>
<summary>TODO</summary>
	- ETL job  
	- Backend managment page 
	- Dynamic map 
	- DB configuration 
</details>
