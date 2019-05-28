import inspect
import os
import json

import requests
import numpy as np
import pandas as pd

from DBaaS import sakila_graphql

dir_path = os.path.dirname(os.path.realpath(__file__))

URL = "http://localhost:5001/graphql"

QUERIES = [(func, name) for name, func in inspect.getmembers(sakila_graphql) if 'query' in name]


def run():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data_frame = pd.DataFrame(columns=['Query', 'Time', 'Records'])
    for query, name in QUERIES:
        data = dict(query=query)
        response = requests.post(URL, data=json.dumps(data), headers=headers)
        data_frame.loc[-1] = [name, response.elapsed.total_seconds(), length(response)]
        data_frame.index = data_frame.index + 1
        data_frame = data_frame.sort_index()
    print(data_frame)


def length(response):
    data = response.json()
    for _, value in data['data'].items():
        for key, sub_value in value.items():
            if key == "nodes":
                return len(sub_value)
    return 0


if __name__ == "__main__":
    run()
