# -*- coding=utf-8 -*-

import networkx as nx
import osmnx as ox
import argparse
import pprint as pp
import random
import os
import time
import pandas as pd
import numpy as np
import geohash

ox.config(use_cache=True, log_console=False, log_file=True)


def load_road_graph(graph_filename):
    start_time = time.time()
    G = ox.load_graphml(graph_filename)
    print('loaded graph in {:.2f} seconds'.format(time.time() - start_time))
    number_of_nodes = G.number_of_nodes()
    number_of_edges = G.number_of_edges()
    print('number of nodes: {}, number of edges: {}'.format(number_of_nodes, number_of_edges))
    return G

def main(args):
    pastart_time = time.time()
    # 加载路网图
    graph_file = args['graph_file']
    G = load_road_graph(graph_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph_file", type=str, default="", help="the graph file")
    args = vars(parser.parse_args())
    pp.pprint(args)
    main(args)