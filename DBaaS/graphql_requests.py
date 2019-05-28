import inspect
import os
import json

import requests
import pandas as pd

from DBaaS import sakila_graphql
from DBaaS import eosm_ch_graphql

dir_path = os.path.dirname(os.path.realpath(__file__))

SAKILA_URL = "http://localhost:5001/graphql"
EOSM_URL = "http://localhost:5002/graphql"
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

SAKILA_QUERIES = [(func, name) for name, func in inspect.getmembers(sakila_graphql) if 'query' in name]
EOSM_QUERIES = [(func, name) for name, func in inspect.getmembers(eosm_ch_graphql) if 'query' in name]


def run():
    execute(SAKILA_QUERIES, SAKILA_URL, 'SAKILA')
    execute(EOSM_QUERIES, EOSM_URL, 'EOSM')


def execute(queries, url, title):
    data_frame = pd.DataFrame(columns=['Query', 'Time', 'Records'])
    print(title)
    for query, name in queries:
        data = dict(query=query)
        response = requests.post(url, data=json.dumps(data), headers=HEADERS)
        data_frame.loc[-1] = [name, response.elapsed.total_seconds(), length(response)]
        data_frame.index = data_frame.index + 1
        data_frame = data_frame.sort_index()
    print(data_frame)
    print()


def length(response):
    data = response.json()
    for _, value in data['data'].items():
        for key, sub_value in value.items():
            if key == "nodes":
                return len(sub_value)
    return 0


if __name__ == "__main__":
    run()
