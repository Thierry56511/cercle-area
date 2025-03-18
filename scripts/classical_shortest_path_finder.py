#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find the shortest path between 2 points in a graph with Dijkstra or A*.
"""

import argparse
import os
from my_research.utils.grid_dijkstra import (dijkstra_stepwise, astar_stepwise, heuristic)

def _build_arg_parser():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument("--input", type=str, required=True, help="Name of the file JSON containing the graph")
    p.add_argument("--shortestpath", type=str, required=True, help="Name of the file JSON containing the graph")
    return p

def main():
    parser = _build_arg_parser()
    args = parser.parse_args()

    grid, G = generer_grille(args.size, args.obstacle_mode, args.obstacle_ratio, args.obstacle_number)
    save_graphe(G, args.output)
    # Afficher la grille générée et les noeuds du graph
    print("Grille générée :")
    print(grid)
    print("Graph nodes:", list(G.nodes))

if __name__ == "__main__":
    main()
