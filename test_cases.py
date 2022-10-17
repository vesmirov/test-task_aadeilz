"""Module with cases for unit tests

Describes:
- cases with valid parameters for Paginator (*kwargs*) and expected result (*result*)
- cases with invalid parameters for Paginator and expected error (*error*)
"""

valid_cases = (
    {
        'kwargs': {'current_page': 4, 'total_pages': 5, 'boundaries': 1, 'around': 0},
        'result': '1 ... 4 5',
    },
    {
        'kwargs': {'current_page': 3, 'total_pages': 5, 'boundaries': 0, 'around': 0},
        'result': '... 3 ...',
    },
    {
        'kwargs': {'current_page': 1, 'total_pages': 10, 'boundaries': 1, 'around': 0},
        'result': '1 ... 10',
    },
    {
        'kwargs': {'current_page': 1, 'total_pages': 10, 'boundaries': 0, 'around': 0},
        'result': '1 ...',
    },
    {
        'kwargs': {'current_page': 10, 'total_pages': 10, 'boundaries': 0, 'around': 0},
        'result': '... 10',
    },
    {
        'kwargs': {'current_page': 1, 'total_pages': 1, 'boundaries': 0, 'around': 0},
        'result': '1',
    },
    {
        'kwargs': {'current_page': 4, 'total_pages': 10, 'boundaries': 2, 'around': 2},
        'result': '1 2 3 4 5 6 ... 9 10',
    },
    {
        'kwargs': {'current_page': 10000, 'total_pages': 100000, 'boundaries': 3, 'around': 5},
        'result': '1 2 3 ... 9995 9996 9997 9998 9999 10000 10001 10002 10003 10004 10005 ... 99998 99999 100000',
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 0},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 0, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 7, 'around': 0},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'kwargs': {'current_page': 1, 'total_pages': 1, 'boundaries': 1, 'around': 1},
        'result': '1'
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10},
        'result': '1 2 3 4 5 6 7 ... 9 10'
    },
    {
        'kwargs': {'current_page': 6, 'total_pages': 13},
        'result': '1 2 ... 4 5 6 7 8 ... 12 13'
    },
)

invalid_cases = (
    {
        'kwargs': {},
        'error': TypeError,
    },
    {
        'kwargs': {'boundaries': 1, 'around': 1},
        'error': TypeError,
    },
    {
        'kwargs': {'current_page': 0, 'total_pages': 10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 1, 'total_pages': 0, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 11, 'total_pages': 10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': -5, 'total_pages': -10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': -2, 'around': -100},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': None, 'total_pages': None},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': '5', 'total_pages': '10'},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': None, 'around': None},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': '2', 'around': '3'},
        'error': ValueError,
    },
)
