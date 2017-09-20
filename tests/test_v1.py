import pytest

from routed_flow.v1 import rev
from routed_flow.v1 import upstream


flow1 = rev([
    '    ',
    '    ',
    '    ',
    '    ',
])

flow2 = rev([
    'S   ',
    'S   ',
    'S   ',
    'S   ',
])

flow3 = rev([
    ' S  ',
    'ES S',
    ' ESW',
    '  S ',
])


@pytest.mark.parametrize('flow, i, j, expected', [
    (flow1, 0, 0, []),
    (flow2, 0, 1, []),
    (flow2, 0, 0, [(1,0), (2,0), (3,0)]),
    (flow3, 0, 2, [(1,1), (1,2), (1,3), (2,0), (2,1), (2,3), (3,1)]),
    (flow3, 1, 2, [(1,1), (1,3), (2,0), (2,1), (2,3), (3,1)]),
    (flow3, 2, 1, [(2,0), (3,1)]),
])
def test_upstream(flow, i, j, expected):
    print()
    assert sorted(upstream(flow, i, j)) == sorted(expected)
