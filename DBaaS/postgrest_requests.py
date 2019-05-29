import inspect

import requests
import pandas as pd

from DBaaS import sakila_postgrest, eosm_ch_postgrest

SAKILA_URL = "http://localhost:3000/"
EOSM_URL = "http://localhost:3001/"
HEADERS = {'Range-Unit': 'items', 'Accept': 'application/json'}

SAKILA_QUERIES = [(func, name) for name, func in inspect.getmembers(sakila_postgrest) if 'query' in name]
EOSM_QUERIES = [(func, name) for name, func in inspect.getmembers(eosm_ch_postgrest) if 'query' in name]


def run():
    execute(SAKILA_QUERIES, SAKILA_URL, 'SAKILA')
    execute(EOSM_QUERIES, EOSM_URL, 'EOSM')


def execute(queries, url, title):
    data_frame = pd.DataFrame(columns=['Query', 'Time', 'Records'])
    print(title)
    for query, name in queries:
        request_url = url + query
        response = requests.get(request_url, headers=HEADERS)
        data = response.json()
        data_frame.loc[-1] = [name, response.elapsed.total_seconds(), len(data)]
        data_frame.index = data_frame.index + 1
        data_frame = data_frame.sort_index()
    print(data_frame)
    print()


if __name__ == "__main__":
    run()
