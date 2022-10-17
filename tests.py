import unittest

from pagination import Paginator
from test_cases import valid_cases, invalid_cases


class TestPaginator(unittest.TestCase):
    def test_valid_cases(self):
        for case in valid_cases:
            with self.subTest(msg=f'passed arguments: {case["kwargs"]}'):
                paginator = Paginator(**case['kwargs'])
                result = paginator.get_pages()
                self.assertEqual(result, case['result'])

    def test_invalid_cases(self):
        for case in invalid_cases:
            with self.subTest(msg=f'passed arguments: {case["kwargs"]}'):
                with self.assertRaises(case['error']):
                    Paginator(**case['kwargs'])


if __name__ == '__main__':
    unittest.main()
