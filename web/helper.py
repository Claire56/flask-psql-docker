import json
from datetime import datetime as dt




class Utilities:
    column_names = ['date','slot_id', 'desktop', 'impressions']
    input_file = 'api/inputdata.json'

def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

def get_date(string_date):
    date = dt.strptime(string_date, '%d/%m/%Y').date()
    return date

def build_advert_sql_query(json_payload):
    query = "SELECT * FROM advertisings WHERE "
    filter_list = json_payload['filter']
    # device_list = json_payload['device']
    start_time_param = json_payload['start_time'] 
    start_time_param = json_payload['end_time'] 
    group_by_list = json_payload['group_by']
    
    filter_cyle = iter(filter_list)
    filter_params = 'slot_id == ' + next(filter_cyle)
    while True:
        filter_params = ' OR slot_id == ' + next(filter_cyle)
    
    device_cycle = cycle(device_list)
    device_params = 'device == ' + next(device_cycle)
    while True:
        device_params = ' OR device == ' + next(device_cyle)
        
    
    group_by_cycle = iter(group_by_list)
    group_by_params = 'group by ' + next(group_by_cycle)
    group_by_params = 'group by ' + group_by_list[0] + ","+ group_by_list[1]
    while True:
        group_by_params = " , " + next(group_by_cyle)
    
    query = query + fitler_params + device_params + group_by_params
    query = query + fitler_params + group_by_params
    return query


def build_advert_query(json_payload):
    query = "SELECT * FROM advertisings ads WHERE "
    filter_list = json_payload['filter']
    # device_list = json_payload['device']
    filters = "ads.date BETWEEN ("+ json_payload['start_time'] + " and "
    filter1 = json_payload['end_time'] + ") AND slot_id = " + str(filter_list['slot_id'][0]) 
    filter3 = " AND device in (" + filter_list['device'][0] + ","+ filter_list['device'][1] + ") GROUP BY "
    groupby = json_payload['group_by'][0] + "," + json_payload['group_by'][1] + ";"
    
    query = query + filters + filter1 + filter3 
    return query