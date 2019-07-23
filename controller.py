import urllib, json
import pandas as pd
import datetime as dt 
''' 
ref :  https://github.com/JTLX/SGTaxiHeatMap/blob/master/update_heat.py
ref :  https://data.gov.sg/developer
ref :  https://data.gov.sg/api/1/util/snippet/api_info.html?resource_id=31ca0cee-6d9e-453a-8b4f-376d37713a10&datastore_root_url=https%3A%2F%2Fdata.gov.sg%2Fapi%2Faction
ref :  http://harrywood.co.uk/maps/examples/leaflet/marker-array.view.html
'''

def call_taxi_api():
    request_headers = {"api-key": "gWpVyvnoSuAeW1J27L7W4nNG4gbQwfVC"}
    request = urllib.request.Request('https://api.data.gov.sg/v1/transport/taxi-availability',headers=request_headers)
    response = urllib.request.urlopen(request)
    # Convert HTTPResponse object to dictionary
    result = json.loads(response.read().decode('utf-8'))
    return result, response

def taxi():
    result, response = call_taxi_api()
    (json.loads(json.dumps(result, ensure_ascii=False)))
    data = result['features'][0]['geometry']['coordinates']
    df = pd.DataFrame(result['features'][0]['geometry']['coordinates'])
    df.columns = ['lon', 'lat']
    df['timestamp']=dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    df_=[]
    for k in data:
        df_.append(k[::-1])
    for k in df_:
        k.append(0.5)
    print (df)    
    return (df_)
