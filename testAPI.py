from flask import Flask, jsonify, request
import os
import pandas as pd
import json

app = Flask(__name__)

test_type = ''
start = False
results = []

# starting dictionary - will change this when add database
start_test = {'test_type' :  test_type , 'is_done' : start}


# start tests with PUT  
@app.route('/api/v1/login/<string:test_name>' , methods = ['PUT'])
def startTest(test_name):
	start_test['test_type'] = test_name
	start_test['is_done'] = True

	# run test 
	os.system('python testSuite_' + test_name + '.py')
	
	return jsonify(start_test)


if __name__ == '__main__':
	app.run(debug=True, port =8080)