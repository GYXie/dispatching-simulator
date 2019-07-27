import osmnx as ox
import matplotlib.pyplot as plt

ox.config(use_cache=True, log_console=False, log_file=True)

if __name__ == '__main__':
    G = ox.graph_from_place('Manhattan Island, New York City, New York, USA', network_type='drive')
    # ox.plot_graph(G)
    fig, ax = ox.plot_graph(G, node_size=1, node_color='g', save=False, edge_linewidth=0.3, fig_height=20,
                            bgcolor='k', show=False)
    fig.savefig('Manhattan.png', dpi=300)