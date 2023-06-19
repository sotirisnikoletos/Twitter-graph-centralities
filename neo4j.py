import csv
import networkx as nx
import community
import pandas as pd
#create graph from txt



mapping_file = "tweets0text1.txt"
user_mapping = {}
with open(mapping_file, "r") as f:
    for line in f:
        parts = line.strip().split(",")
        node_id = parts[0].strip().strip('"')
        username = parts[2].strip().strip('"')
        user_mapping[node_id] = username
        if line == 47229:
            break



filename = "tweets.txt"  
edges = []
with open(filename, 'r') as f:
    
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            
            edges.append((row[0], row[1], int(row[3])))

tweets_graph = nx.DiGraph()
output_file = "terminal_output22.txt"
with open(output_file, "w") as f:
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
        nodes.add(edge[2])
    tweets_graph.add_nodes_from(nodes)

    for edge in edges:
        source, target, weight = edge
        tweets_graph.add_edge(source, target, weight=weight)
    print(tweets_graph.number_of_edges())
    print(tweets_graph.number_of_nodes())

    components = nx.strongly_connected_components(tweets_graph)
    largest_component = max(components, key=len)
    H = max(nx.connected_component_subgraphs(tweets_graph), key=len)




    centrality = nx.betweenness_centrality(H,weight=edge[2])

    for key, value in centrality.items():
        print(f"{key}: {value}")
    top_10_values = sorted(centrality.values(), reverse=True)[:10]
    top_10_keys =[key for key, value in centrality.items() if value in top_10_values]
    usernames = [user_mapping.get(node, node) for node in top_10_keys]
    for value, key in zip(top_10_values, top_10_keys):
        print(f"Value: {value}, Key: {key}",file=f)

    print(H.number_of_nodes())
    print(H.number_of_edges())

    centrality = nx.pagerank(H,weight=edge[2])

    for key, value in centrality.items():
        print(f"{key}: {value}")
    top_10_values = sorted(centrality.values(), reverse=True)[:10]
    top_10_keys =[key for key, value in centrality.items() if value in top_10_values]
    usernames = [user_mapping.get(node, node) for node in top_10_keys]
    for value, key in zip(top_10_values, top_10_keys):
        print(f"Value: {value}, Key: {key}",file=f)


        centrality = nx.closeness_centrality(H)


    top_10_values = sorted(centrality.values(), reverse=True)[:10]
    top_10_keys =[key for key, value in centrality.items() if value in top_10_values]
    usernames = [user_mapping.get(node, node) for node in top_10_keys]
    for value, key in zip(top_10_values, top_10_keys):
        print(f"Value: {value}, Key: {key}",file=f)