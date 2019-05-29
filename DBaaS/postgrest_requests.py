import inspect

import requests
import pandas as pd

from DBaaS import sakila_postgrest, eosm_ch_postgrest

SAKILA_URL = "http://localhost:3000/"
EOSM_URL = "http://localhost:3001/"
HEADERS = {'Range-Unit': 'items', 'Accept': 'application/json'}

SAKILA_QUERIES = [(func, name) for name, func in inspect.getmembers(sakila_postgrest) if 'query' in name]
EOSM_QUERIES = [(func, name) for name, func in inspect.getmembers(eosm_ch_postgrest) if 'query' in name]

REPETITIONS = 1


def run():
    sakila_df = execute(SAKILA_QUERIES, SAKILA_URL, 'SAKILA PostgREST')
    eosm_df = execute(EOSM_QUERIES, EOSM_URL, 'EOSM PostgREST')
    return [sakila_df, eosm_df]


def execute(queries, url, title):
    data_frame = pd.DataFrame(columns=['Query', 'AvgTime', 'Records'])
    print(title)
    for query, name in queries:
        request_url = url + query
        average_time, response = average_of_multiple_requests(request_url, REPETITIONS, HEADERS)
        nr_entries = length(response)
        data_frame.loc[-1] = [name, average_time, nr_entries]
        data_frame.index = data_frame.index + 1
        data_frame = data_frame.sort_index()
    print(data_frame)
    print()
    return data_frame


def average_of_multiple_requests(url, repetitions, headers):
    response = None
    time_sum = 0
    for i in range(repetitions):
        response = requests.get(url, headers=headers)
        time_sum += response.elapsed.total_seconds()
    return (time_sum / repetitions), response


def length(response):
    data = response.json()
    return len(data)


if __name__ == "__main__":
    run()
