## SG taxi heatmap 




LIVE VIEW : <http://ec2-35-167-225-131.us-west-2.compute.amazonaws.com:5000/>

demo :  
		![image](https://github.com/yennanliu/SGTaxiMap/blob/master/data/taxi_location.png)
		![image](https://github.com/yennanliu/SGTaxiMap/blob/master/data/heatmap.png)




## Run the heatmap :

step 1 

```Bash
# get repo 
git clone https://github.com/yennanliu/SGTaxiMap
cd SGTaxiMap

```

step 2 

```Bash
python run.py
```
```
# view the heatmap via browser 
visit http://127.0.0.1:5000 
```


## Data collect :

```Bash 
# can modify cron job in /crontab.txt 
# collected data can either saved as csv or DB 
 /anaconda/envs/<your_dev_env>/bin/python etl/job_luigi.py   Agg_taxi_locations

```

## Reference 

- Open source projct 
	- https://github.com/JTLX/SGTaxiHeatMap/blob/master/update_heat.py
	- https://data.gov.sg/developer
	- https://data.gov.sg/api/1/util/snippet/api_info.html?resource_id=31ca0cee-6d9e-453a-8b4f-376d37713a10&datastore_root_url=https%3A%2F%2Fdata.gov.sg%2Fapi%2Faction
	- http://harrywood.co.uk/maps/examples/leaflet/marker-array.view.html

- Automated heat map 
	- http://rmaps.github.io/blog/posts/animated-choropleths/index.html




