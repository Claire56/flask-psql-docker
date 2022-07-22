from flask import Flask, request, jsonify, render_template
import sqlite3 as sqlite
# from flask_negotiate import consumes, produces
import sys , os,json
from helper import build_advert_query, build_advert_sql_query
import model

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return """<h1>ML project</h1>
    <p>A prototype API to filter data </p>
    """
@app.route('/alldata', methods=['GET'])
def all_data():
    conn = sqlite.connect('../api/advertisings.db')
    cur = conn.cursor()
    all_data = cur.execute("SELECT * FROM advertisings;").fetchall()
    return jsonify(all_data) 
@app.route('/alldata2', methods=['GET'])
def all_data2():
    all_data = model.Advert.Query.all().fetchall()
    return jsonify(all_data) 

@app.route('/request_data', methods=['POST'])
def request_data():
    data = request.json
    print("#####################################################")
    print(data)
    end_time = data['end_time']
    start_time = data['start_time']
    filter_list = data['filter']
    group_by_list = data['group_by']
    slot_id = filter_list['slot_id'][0]
    sql_query = build_advert_query(data)
    print(sql_query)

    conn = sqlite.connect('../api/advertisings.db')
    cur = conn.cursor()
    get_data = cur.execute(sql_query).fetchall()
    
    return jsonify(get_data) 

@app.route('/request_data1', methods=['POST'])
# @consumes('application/json')
# @produces('application/json')
def request_data1():
    json_payload = request.json
    print('###########################################')
    print(json_payload)
    
    if ( (json_payload['filter'] == None) or
        #  (json_payload['device'] == None) or
         (json_payload['start_time'] == None) or
         (json_payload['end_time'] == None) or
         (json_payload['group_by'] == None) ) :
        
        return "Sorry, we only take Json"
    else:
        sql_query = build_advert_sql_query(json_payload)
        
    conn = sqlite.connect('../api/advertisings.db')
    cur = conn.cursor()
    all_data = cur.execute(sql_query).fetchall()
    return jsonify(all_data) 

@app.errorhandler(404)
def page_not_found(e):
    return """<h1> Ohh no :(</h1>
    <h3> We dont have that route please check your entry</h3>
    """


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

