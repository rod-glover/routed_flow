import numpy as np

def rev(l):
    return list(reversed(l))


flow_from = rev([
    ' S ',
    'E W',
    ' N ',
])


def upstream(flow, i, j):
    """Given a flow matrix, return a list of indexes of all cells upstream
    of cell (i, j)."""
    upstream_neigbours = []
    for di, dj in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
        # print('({}, {}) testing ({}, {})'.format(i, j, i+di, j+dj))
        try:
            nbr_flow = flow[i+di][j+dj]
        except IndexError:
            # print('      outside')
            pass
        else:
            # print('      {} ? {}'.format(nbr_flow, flow_from[di+1][dj+1]))
            if nbr_flow == flow_from[di+1][dj+1]:
                # print('         adding ({}, {})'.format(i+di, j+dj))
                upstream_neigbours.append((i+di, j+dj))
                upstream_neigbours.extend(upstream(flow, i+di, j+dj))
    return upstream_neigbours