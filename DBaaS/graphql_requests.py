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
REPETITIONS = 10


def run():
    sakila_df = execute(SAKILA_QUERIES, SAKILA_URL, 'SAKILA Postgraphile')
    eosm_df = execute(EOSM_QUERIES, EOSM_URL, 'EOSM Postgraphile')
    return [sakila_df, eosm_df]


def execute(queries, url, title):
    data_frame = pd.DataFrame(columns=['Query', 'AvgTime', 'Records'])
    print(title)
    for query, name in queries:
        data = dict(query=query)
        average_time, response = average_of_multiple_requests(url, data, REPETITIONS, HEADERS)
        data_frame.loc[-1] = [name, average_time, length(response)]
        data_frame.index = data_frame.index + 1
        data_frame = data_frame.sort_index()
    print(data_frame)
    print()
    return data_frame


def average_of_multiple_requests(url, data, repetitions, headers):
    response = None
    time_sum = 0
    data = json.dumps(data)
    for i in range(repetitions):
        response = requests.post(url, data=data, headers=headers)
        time_sum += response.elapsed.total_seconds()
    return (time_sum / repetitions), response


def length(response):
    data = response.json()
    for _, value in data['data'].items():
        for key, sub_value in value.items():
            if key == "nodes":
                return len(sub_value)
    return 0


if __name__ == "__main__":
    run()
