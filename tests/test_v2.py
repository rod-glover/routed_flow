import pytest

from routed_flow import rev, to_visual_directions, upstream


flow0 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


flow1 = rev([
    [5, 0, 0, 6],
    [3, 3, 5, 0],
    [0, 0, 6, 8],
    [0, 9, 0, 1],
])


def print_visual(flow):
    for row in rev(to_visual_directions(flow)):
        print(''.join(row))


@pytest.mark.parametrize('flow, i, j, expected', [
    (flow0, 1, 1, []),
    (flow1, 0, 1, [
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 2),
        (3, 0),
        (3, 3),
    ]),
    (flow1, 2, 2, [
        (0, 3),
        (1, 3),
        (2, 0),
        (2, 1),
        (3, 0),
        (3, 3),
    ])
])
def test_upstream(flow, i, j, expected):
    print()
    print_visual(flow)

    upstream_cells = upstream(flow, i, j)
    assert sorted(upstream_cells) == sorted(expected)

    def upstream_cell(i, j, k, l):
        if (i, j) == (k, l):
            return 9
        if (k, l) in upstream_cells:
            return flow[k][l]
        return 0
    upstream_flow = [
        [upstream_cell(i, j, k, l) for l, col in enumerate(row)]
        for k, row in enumerate(flow)
    ]

    print('----')
    print_visual(upstream_flow)