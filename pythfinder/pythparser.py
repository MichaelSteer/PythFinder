"""pythparser.py Argument parser for pythfinder
"""

import argparse

ACCEPTABLE_T = ("U", "D")
ALGORITHM_SET = ("dfs", "bfs", "astar", "dijkstra", "fwarshall")


class ArgParser(object):

    args = None

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='Traverse a graph')

        # Graph Type
        parser.add_argument('-g', metavar='g', type=str, nargs=1,
                            help='The type of graph to process. U is undirected,'
                                 'D is directed',
                            choices=set(ACCEPTABLE_T))

        # Algorithm Type
        parser.add_argument('-a', metavar='a', type=str, nargs=1,
                            help='The Algorithm to use to solve the graph. several options are available',
                            choices=set(ALGORITHM_SET))

        args = parser.parse_args()
        return args

    @staticmethod
    def process(args):
        print(args.g[0])
        if not (args.g[0] in ACCEPTABLE_T):
            print("Bad Graph Type: {}".format(args.t[0]))
            return False
        print(args.a[0])
        if not (args.a[0] in ALGORITHM_SET):
            print("Bad Algorithm Type {}".format(args.a[0]))
        return True
