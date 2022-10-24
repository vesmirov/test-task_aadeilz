#!/usr/bin/env python3

ELLIPSIS = '...'


class Paginator:
    """
    Allows to get a string with pagination, which is built based on the given parameters:
    :current_page: - active page (mandatory)
    :total_pages: - total number of pages (mandatory)
    :boundaries: - how many pages should be displayed around the edges of the first and last page (default 1)
    :around: - how many pages should be displayed around the active page (default 1)

    The line is build from three parts: head, body, and tail.
    Those represent the first page with boundary pages, the active page with around pages,
    and the last page with boundary pages.

    use ``.get_pages()`` method for getting the string with pagination
    or  ``.print_pages()`` to print them directly
    """

    def __init__(self, current_page, total_pages, boundaries=1, around=1):
        self._validate(current=current_page, total=total_pages, boundaries=boundaries, around=around)
        self.current = int(current_page)
        self.total = int(total_pages)
        self.boundaries = int(boundaries)
        self.around = int(around)

    @staticmethod
    def _validate(**kwargs):
        for value in kwargs.values():
            if not ((isinstance(value, int) or isinstance(value, str)
                     and value.isnumeric()) and int(value) >= 0):
                raise ValueError('Arguments must be either positive integer or zero')

        if not (kwargs['current'] and kwargs['total']):
            raise ValueError('"current_page" and "total_pages" cannot be zero')

        if int(kwargs['current']) > int(kwargs['total']):
            raise ValueError('"total_page" cannot be lower than "current_page"')

    def _get_body_edges(self):
        left = self.current - self.around
        right = self.current + self.around

        return (left if left > 1 else 1,
                right if right < self.total else self.total)

    def _get_head(self, left_body_edge):
        if not self.boundaries:
            return [ELLIPSIS] if left_body_edge > 1 else []

        if self.boundaries >= left_body_edge - 1:
            return list(map(str, range(1, left_body_edge)))

        return list(map(str, range(1, self.boundaries + 1))) + [ELLIPSIS]

    def _get_tail(self, right_body_edge):
        if not self.boundaries:
            return [ELLIPSIS] if right_body_edge < self.total else []

        left_tail_edge = self.total - self.boundaries
        if left_tail_edge <= right_body_edge:
            return list(map(str, range(right_body_edge + 1, self.total + 1)))

        return [ELLIPSIS] + list(map(str, range(left_tail_edge + 1, self.total + 1)))

    def get_pages(self):
        left_body_edge, right_body_edge = self._get_body_edges()
        head = ' '.join(self._get_head(left_body_edge))
        body = ' '.join(map(str, range(left_body_edge, right_body_edge + 1)))
        tail = ' '.join(self._get_tail(right_body_edge))

        return ' '.join(filter(None, [head, body, tail]))

    def print_pages(self):
        print(self.get_pages())


if __name__ == '__main__':
    args = input('Give me four numbers <current_page> <total_pages> '
                 '<boundaries> <boundaries>: ').split()[:4]
    Paginator(*args).print_pages()
