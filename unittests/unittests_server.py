import os
import json
from flask import Flask, Response, request

app = Flask(__name__, root_path='testdata')

not_found_json = '{"Message": "resource not found"}'
project_ids_files = {
    "43378a5d48364f9d8cf3c3d5104df560": "project_valid_0.json",
    "38n54mgtogq4nq2s5nfqcoop4160vso7": "project_invalid_0.json"
}

study_ids_files = {}
expression_ids_files = {}

data_dir = "unittests/testdata/json_instances/"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/projects/search")
def search_project():

    matches = []
    possible_filters = ["version", "name"]

    for f in project_ids_files.values():
        json_file = data_dir + f
        json_s = open(json_file, "r").read()
        json_obj = json.loads(json_s)
        add_to_matches = True

        for filter_name in possible_filters:
            filter_val = request.args.get(filter_name)
            if filter_val:
                if json_obj[filter_name] != filter_val:
                    add_to_matches = False
        
        if add_to_matches:
            matches.append(json_s)

    return "[" + ",".join(matches) + "]"

@app.route("/projects/<project_id>")
def get_project(project_id):
    
    response = None
    if project_id in project_ids_files.keys():
        json_file = data_dir + project_ids_files[project_id]
        if os.path.exists(json_file):
            response = Response(open(json_file, "r").read(), status=200)
        else:
            response = Response(not_found_json, status=404)
    else:
        if project_id == "NA": # endpoint not implemented simultation,
                               # return 501 instead of 404
            response = Response(not_found_json, status=501)
        else:    
            response = Response(not_found_json, status=404)
    
    return response

@app.route("/studies/<study_id>")
def get_study(study_id):
    response = None
    if study_id in study_ids_files.keys():
        json_file = data_dir + study_ids_files[study_id]
        if os.path.exists(json_file):
            response = Response(open(json_file, "r").read(), status=200)
        else:
            response = Response(not_found_json, status=404)
    else:
        if study_id == "NA": # endpoint not implemented simultation,
                               # return 501 instead of 404
            response = Response(not_found_json, status=501)
        else:    
            response = Response(not_found_json, status=404)
    
    return response

@app.route("/expressions/<expression_id>")
def get_expression(expression_id):
    response = None
    if expression_id in expression_ids_files.keys():
        json_file = data_dir + expression_ids_files[expression_id]
        if os.path.exists(json_file):
            response = Response(open(json_file, "r").read(), status=200)
        else:
            response = Response(not_found_json, status=404)
    else:
        if expression_id == "NA": # endpoint not implemented simultation,
                               # return 501 instead of 404
            response = Response(not_found_json, status=501)
        else:    
            response = Response(not_found_json, status=404)
    
    return response