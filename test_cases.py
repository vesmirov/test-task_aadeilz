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
        'result': '1 ... 5',
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
        'kwargs': {'current_page': 1, 'total_pages': 1, 'boundaries': 100, 'around': 100},
        'result': '1',
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'kwargs': {'current_page': 4, 'total_pages': 10, 'boundaries': 2, 'around': 2},
        'result': '1 2 3 4 5 6 ... 9 10',
    },
    {
        'kwargs': {'current_page': 7, 'total_pages': 15},
        'result': '1 2 3 ... 5 6 7 8 9 ... 13 14 15',
    },
)

invalid_cases = (
    {
        'kwargs': {},
        'error': TypeError,
    },
    {
        'kwargs': {'boundaries': 2, 'around': 3},
        'error': TypeError,
    },
    {
        'kwargs': {'current_page': 0, 'total_pages': 10},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 1, 'total_pages': 0},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 11, 'total_pages': 10},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': -5, 'total_pages': -10},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': -2, 'around': -3},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': None, 'total_pages': None},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': None, 'around': None},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': '5', 'total_pages': '10'},
        'error': ValueError,
    },
    {
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': '2', 'around': '3'},
        'error': ValueError,
    },
)
