import os

import pandas as pd
import matplotlib.pyplot as plt

from DBaaS.postgrest_requests import run as postgrest_run
from DBaaS.graphql_requests import run as graphql_run

dir_path = os.path.dirname(os.path.realpath(__file__))


def run():
    postgrest_data_frames = postgrest_run()
    postgrest_titles = ['SAKILA_PostgREST', 'EOSM_PostgREST']
    for df, title in zip(postgrest_data_frames, postgrest_titles):
        save_df_plot(df, title)
        save_df(df, title)
    graphql_data_frames = graphql_run()
    graphql_titles = ['SAKILA_Postgraphile', 'EOSM_Postgraphile']
    for df, title in zip(graphql_data_frames, graphql_titles):
        save_df_plot(df, title)
        save_df(df, title)


def save_df_plot(data_frame, title, show=False):
    df = pd.DataFrame({'Query': data_frame['Query'], 'AvgTime [s]': data_frame['AvgTime']})
    df.plot.bar(x='Query', y='AvgTime [s]', rot=90, title=title)
    path = os.path.join(dir_path, 'results')
    path = os.path.join(path, title + '.png')
    plt.savefig(path)
    if show:
        plt.show()


def save_df(data_frame, title):
    path = os.path.join(dir_path, 'results')
    path = os.path.join(path, title + '.csv')
    data_frame.to_csv(path, encoding='utf-8')


if __name__ == "__main__":
    run()
