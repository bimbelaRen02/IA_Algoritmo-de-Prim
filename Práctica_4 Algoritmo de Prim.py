import matplotlib.pyplot as plt
import networkx as nx

# Grafo de prueba (modificable)
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

# Función para dibujar el grafo y actualizar el MST parcial
def draw_step(G, pos, mst_edges, title):
    plt.clf()  # Limpia la figura actual
    # Colores: rojo para todos, azul para el MST
    edge_colors = ['blue' if (u, v) in mst_edges or (v, u) in mst_edges else 'gray' for u, v in G.edges()]
    
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color=edge_colors,
            node_size=1000, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    plt.pause(1)  # Espera para mostrar paso a paso

# Algoritmo de Prim con trazado gráfico y consola
def prim(graph, start):
    print(f"Iniciando algoritmo de Prim desde el nodo '{start}'")
    
    # Crear el grafo en networkx
    G = nx.Graph()
    for u in graph:
        for v, w in graph[u].items():
            G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)  # Posición de nodos para graficar
    
    visited = set()        # Conjunto de nodos visitados
    mst_edges = []         # Lista de aristas del árbol mínimo
    edges = []             # Cola de prioridades (lista de candidatos)
    
    visited.add(start)
    print(f"Agregando nodo inicial '{start}' al árbol")
    
    # Agrega las aristas del nodo inicial a la lista
    for to, cost in graph[start].items():
        edges.append((cost, start, to))
    
    draw_step(G, pos, mst_edges, "Inicio del algoritmo de Prim")
    
    while edges:
        # Ordenamos la lista de aristas por su peso (Prim no usa heap obligatoriamente)
        edges.sort()
        cost, frm, to = edges.pop(0)  # Sacamos la arista más barata

        if to in visited:
            continue  # Si ya fue visitado, lo ignoramos

        # Agregamos la arista al MST
        visited.add(to)
        mst_edges.append((frm, to))
        print(f"✔️ Se agrega la arista ({frm} - {to}) con peso {cost} al MST")
        
        # Agregamos las nuevas aristas del nodo recién visitado
        for neighbor, weight in graph[to].items():
            if neighbor not in visited:
                edges.append((weight, to, neighbor))
        
        # Actualizar visualización
        draw_step(G, pos, mst_edges, f"Agregando ({frm}-{to}), peso {cost}")

    print("\nÁrbol de expansión mínima completo:")
    for u, v in mst_edges:
        print(f" - {u} -- {v} (peso: {graph[u][v]})")

    # Mostrar resultado final
    draw_step(G, pos, mst_edges, "Árbol de Expansión Mínima Final")
    plt.show()

# Ejecutamos el algoritmo
prim(graph, 'A')