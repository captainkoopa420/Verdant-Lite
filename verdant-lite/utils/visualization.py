import plotly.graph_objects as go
import networkx as nx

def visualize_memory_graph(memory):
    G = memory.graph
    pos = nx.spring_layout(G, seed=42)
    
    # Create edge traces
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
    
    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )
    
    # Create node traces
    node_x = []
    node_y = []
    node_text = []
    node_color = []
    
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        stability = memory.memory_store[node]["stability"]
        node_text.append(f"{node} — Stability: {stability:.2f}")
        node_color.append(stability)
    
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers',
        hoverinfo='text',
        text=node_text,
        marker=dict(
            showscale=True,
            colorscale='YlOrRd',
            reversescale=True,
            color=node_color,
            size=10,
            colorbar=dict(
                thickness=15,
                title="Stability",
                xanchor='left'
            ),
            line_width=2)
    )
    
    # Fix: Replace titlefont_size with title object containing font properties
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title={
                'text': '<b>Verdant Lite: Memory Graph</b>',
                'font': {'size': 16}
            },
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
    )
    
    fig.show()
