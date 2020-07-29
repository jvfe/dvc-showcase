# %%
import networkx as nx
import csv

# %%
def make_edgelist(file, cols=[2, 3], delim="\t"):
    """Create an edgelist that's easy to parse"""
    pairs = []

    with open(file, "r") as inter_file:
        reader = csv.reader(inter_file, delimiter=delim)

        for row in reader:
            pairs.append([row[i] for i in cols])

    interacts = [" ".join(pair) for pair in pairs]

    return interacts


# %%
def extract_metrics(graph):
    """Extract some metrics from a graph object"""

    nodes = list(graph.nodes())
    clustcoef = nx.clustering(graph)
    degrcent = nx.degree_centrality(graph)
    eigncent = nx.eigenvector_centrality(graph)

    metrics = [["node", "clust_coef", "degr_centr", "eign_cent"]]
    for i in nodes:
        metrics.append([i, clustcoef[i], degrcent[i], eigncent[i]])

    return metrics


# %%
interactions = make_edgelist("../results/interactions.tsv")
G = nx.parse_edgelist(interactions)

# %%
metrics = extract_metrics(G)
with open("../results/metrics.csv", "w") as res:
    writer = csv.writer(res)
    writer.writerows(metrics)
