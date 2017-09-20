def rev(l):
    return list(reversed(l))


# Instead of NaN, use 0 to indicate a grid cell that is not in the network.
directions = [
    ' ',       # not in network
    '\u2b06',  # N
    '\u2b08',  # NE
    '\u27a1',  # E
    '\u2b0a',  # SE
    '\u2b07',  # S
    '\u2b0b',  # SW
    '\u2b05',  # W
    '\u2b09',  # NW
    '\u229a'   # outlet
    # '\u2218'   # outlet
]


def to_visual_directions(flow):
    return [[directions[v] for v in row] for row in flow]


flow_from = rev([
    [4, 5, 6],
    [3, 0, 7],
    [2, 1, 8],
])

def upstream(flow, i, j):
    """Given a flow matrix, return a list of indexes of all cells upstream
    of cell (i, j)."""
    upstream_neigbours = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di != 0 or dj != 0:  # exclude the cell being processed
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


