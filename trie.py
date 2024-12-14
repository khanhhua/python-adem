graph = {'Z': {'Y'}, 'Y': {'X', 'V'}, 'X': {'T'}, 'V': {'S', 'R'}, 'B': {'C'}, 'C': set()}

graph_keys = graph.keys()
sorted_keys = sorted([*graph_keys])

# print(sorted_keys)
# Schritt fuer Schritt
# 1. Daten: richtig oder kaputt
# 2. Eingabe fuer vorigen Schritt muss dem naechsten Schritten passen

# Wenn child Wert nicht in der List sorted_keys,
#   a. child Wert ist der Root
#   b. gehen wir in subset rein
#   c. daten ist kaputt

def search(graph, value):
    for key, values in graph.items():
        if value in values:
            return key
    return None

def recursive_search(graph, value):
    parent = search(graph, value)
    if parent == None:
        return value
    else:
        return recursive_search(graph, parent)

print(recursive_search(graph, 'T'))