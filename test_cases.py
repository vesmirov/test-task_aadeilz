"""Module with cases for unit tests

Describes:
- cases with valid parameters for Paginator (*kwargs*) and expected result (*result*)
- cases with invalid parameters for Paginator and expected error (*error*)
"""

valid_cases = (
    {
        'msg': 'test valid: case 1 (no "around")',
        'kwargs': {'current_page': 4, 'total_pages': 5, 'boundaries': 1, 'around': 0},
        'result': '1 ... 4 5',
    },
    {
        'msg': 'test valid: case 2 (no "around")',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 7, 'around': 0},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 3 (no "boundaries" and no "around")',
        'kwargs': {'current_page': 3, 'total_pages': 5, 'boundaries': 0, 'around': 0},
        'result': '... 3 ...',
    },
    {
        'msg': 'test valid: case 4 (no "around" and first page is "active_page")',
        'kwargs': {'current_page': 1, 'total_pages': 10, 'boundaries': 1, 'around': 0},
        'result': '1 ... 10',
    },
    {
        'msg': 'test valid: case 5 (no "boundaries" and no "around", first page is "active_page")',
        'kwargs': {'current_page': 1, 'total_pages': 10, 'boundaries': 0, 'around': 0},
        'result': '1 ...',
    },
    {
        'msg': 'test valid: case 6 (no "boundaries" and no "around", last page is "active_page")',
        'kwargs': {'current_page': 10, 'total_pages': 10, 'boundaries': 0, 'around': 0},
        'result': '... 10',
    },
    {
        'msg': 'test valid: case 7 (no "boundaries" and no "around" for one page only)',
        'kwargs': {'current_page': 1, 'total_pages': 1, 'boundaries': 0, 'around': 0},
        'result': '1',
    },
    {
        'msg': 'test valid: case 8 ("boundaries" and "around" are equal)',
        'kwargs': {'current_page': 4, 'total_pages': 10, 'boundaries': 2, 'around': 2},
        'result': '1 2 3 4 5 6 ... 9 10',
    },
    {
        'msg': 'test valid: case 9 (large numbers for "current_page" and "total_pages")',
        'kwargs': {'current_page': 10000, 'total_pages': 100000, 'boundaries': 3, 'around': 5},
        'result': '1 2 3 ... 9995 9996 9997 9998 9999 10000 10001 10002 10003 10004 10005 ... 99998 99999 100000',
    },
    {
        'msg': 'test valid: case 10 ("boundaries" and "around" both greater than "total_pages")',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 11 ("boundaries" is greater than "total_pages")',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 100, 'around': 0},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 12 ("around" is greater than "total_pages")',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 0, 'around': 100},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 13 (all values are equal to 1)',
        'kwargs': {'current_page': 1, 'total_pages': 1, 'boundaries': 1, 'around': 1},
        'result': '1'
    },
    {
        'msg': 'test valid: case 14 (default values of "boundaries" and "around")',
        'kwargs': {'current_page': 5, 'total_pages': 10},
        'result': '1 ... 4 5 6 ... 10'
    },
    {
        'msg': 'test valid: case 15 (default "boundaries" and "around" with small amount of pages)',
        'kwargs': {'current_page': 1, 'total_pages': 2},
        'result': '1 2'
    },
    {
        'msg': 'test valid: case 16 ("boundaries" and "around" have same value)',
        'kwargs': {'current_page': 2, 'total_pages': 100, 'boundaries': 2, 'around': 2},
        'result': '1 2 3 4 ... 99 100',
    },
    {
        'msg': 'test valid: case 17 (last page is "active_page", sum of boundaries is greater that "total_pages")',
        'kwargs': {'current_page': 10, 'total_pages': 10, 'boundaries': 6, 'around': 1},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 18 (first page is "activ_page", sum of boundaries is greater that "total_pages")',
        'kwargs': {'current_page': 1, 'total_pages': 10, 'boundaries': 6, 'around': 1},
        'result': '1 2 3 4 5 6 7 8 9 10',
    },
    {
        'msg': 'test valid: case 19 (last page is "active_page", "around" does not affect "boundaries")',
        'kwargs': {'current_page': 10, 'total_pages': 10, 'boundaries': 3, 'around': 1},
        'result': '1 2 3 ... 8 9 10',
    },
    {
        'msg': 'test valid: case 20 (first page is "active_page", "around" does not affect "boundaries")',
        'kwargs': {'current_page': 1, 'total_pages': 10, 'boundaries': 3, 'around': 1},
        'result': '1 2 3 ... 8 9 10',
    },

)

invalid_cases = (
    {
        'msg': 'test invalid: case 1 (run without parameters)',
        'kwargs': {},
        'error': TypeError,
    },
    {
        'msg': 'test invalid: case 2 (run without required parameters)',
        'kwargs': {'boundaries': 1, 'around': 1},
        'error': TypeError,
    },
    {
        'msg': 'test invalid: case 3 ("current_page" is 0)',
        'kwargs': {'current_page': 0, 'total_pages': 10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 4 ("total_pages" is 0)',
        'kwargs': {'current_page': 1, 'total_pages': 0, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 5 ("current_page" is greater than "total_pages")',
        'kwargs': {'current_page': 11, 'total_pages': 10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 6 (mandatory params are negative integers)',
        'kwargs': {'current_page': -5, 'total_pages': -10, 'boundaries': 1, 'around': 1},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 7 (non-mandatory params are negative integers)',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': -2, 'around': -100},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 8 (mandatory params are None)',
        'kwargs': {'current_page': None, 'total_pages': None},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 9 (non-mandatory params are None)',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': None, 'around': None},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 10 (mandatory params are strings)',
        'kwargs': {'current_page': 'a', 'total_pages': 'b'},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 11 (non-mandatory params are strings)',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 'a', 'around': 'b'},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 12 (mandatory params are floats)',
        'kwargs': {'current_page': 5.0, 'total_pages': 10.0},
        'error': ValueError,
    },
    {
        'msg': 'test invalid: case 13 (non-mandatory params are floats)',
        'kwargs': {'current_page': 5, 'total_pages': 10, 'boundaries': 2.0, 'around': 3.0},
        'error': ValueError,
    },
)
