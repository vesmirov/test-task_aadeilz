"""Module with cases for unit tests

Describes:
- cases with valid parameters for Paginator (*kwargs*) and expected result (*result*)
- cases with invalid parameters for Paginator and expected error (*error*)
"""

valid_cases = (
    {
        'msg': 'test valid: case 1',
        'kwargs': {'current_page': 4, 'total_pages': 5, 'boundaries': 1, 'around': 0},
        'result': '1 ... 4 5',
    },
    {
        'msg': 'test valid: case 2',
        'kwargs': {'current_page': 3, 'total_pages': 5, 'boundaries': 0, 'around': 0},
        'result': '... 3 ...',
    },
    {
        'msg': 'test valid: case 3',
        'kwargs': {'current_page': 1, 'total_pages': 10, 'boundaries': 1, 'around': 0},
        'result': '1 ... 10',
    },
    {
        'msg': 'test valid: case 4',
        'kwargs': {'current_page': 1, 'total_pages': 10, 'boundaries': 0, 'around': 0},
        'result': '1 ...',
    },
    {
        'msg': 'test valid: case 5',
        'kwargs': {'current_page': 10, 'total_pages': 10, 'boundaries': 0, 'around': 0},
        'result': '... 10',
    },
    {
        'msg': 'test valid: case 6',
        'kwargs': {'current_page': 1, 'total_pages': 1, 'boundaries': 0, 'around': 0},
        'result': '1',
    },
    {
        'msg': 'test valid: case 7',
        'kwargs': {'current_page': 4, 'total_pages': 10, 'boundaries': 2, 'around': 2},
        'result': '1 2 3 4 5 6 ... 9 10',
    },
    {
        'msg': 'test valid: case 8',
        'kwargs': {'current_page': 10000, 'total_pages': 100000, 'boundaries': 3, 'around': 5},
        'result': '1 2 3 ... 9995 9996 9997 9998 9999 10000 10001 10002 10003 10004 10005 ... 99998 99999 100000',
    },
    {
        'msg': 'test valid: case 9',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 10',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 0},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 11',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 0, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 12',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 13',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 7, 'around': 0},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 14',
        'kwargs': {'current_page': 1, 'total_pages': 1, 'boundaries': 1, 'around': 1},
        'result': '1'
    },
    {
        'msg': 'test valid: case 15',
        'kwargs': {'current_page': 5, 'total_pages': 10},
        'result': '1 ... 4 5 6 ... 10'
    },
    {
        'msg': 'test valid: case 16',
        'kwargs': {'current_page': 1, 'total_pages': 2},
        'result': '1 2'
    },
    {
        'msg': 'test valid: case 17',
        'kwargs': {'current_page': 2, 'total_pages': 100, 'boundaries': 2, 'around': 2},
        'result': '1 2 3 4 ... 99 100',
    },
)

invalid_cases = (
    {
        'msg': 'test invalid: run without parameters',
        'kwargs': {},
        'error': TypeError,
    },
    {
        'msg': 'test invalid: run without required parameters',
        'kwargs': {'boundaries': 1, 'around': 1},
        'error': TypeError,
    },
    {
        'msg': 'test invalid: "current_page" is zero',
        'kwargs': {'current_page': 0, 'total_pages': 10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: "total_pages" iz zero',
        'kwargs': {'current_page': 1, 'total_pages': 0, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: "current_page" is greater than "total_pages"',
        'kwargs': {'current_page': 11, 'total_pages': 10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: mandatory params are negative integers',
        'kwargs': {'current_page': -5, 'total_pages': -10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: non-mandatory params are negative integers',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': -2, 'around': -100},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: mandatory params are None',
        'kwargs': {'current_page': None, 'total_pages': None},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: non-mandatory params are None',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': None, 'around': None},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: mandatory params are strings',
        'kwargs': {'current_page': 'a', 'total_pages': 'b'},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: non-mandatory params are strings',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 'a', 'around': 'b'},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: mandatory params are floats',
        'kwargs': {'current_page': 5.0, 'total_pages': 10.0},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: non-mandatory params are floats',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 2.0, 'around': 3.0},
        'error': ValueError,
    },
)
