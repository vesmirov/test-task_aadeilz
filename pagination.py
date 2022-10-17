ELLIPSIS = '...'


class Paginator:
    def __init__(self, current_page, total_pages, boundaries=2, around=2):
        self._validate(current=current_page, total=total_pages, boundaries=boundaries, around=around)
        self.current = int(current_page)
        self.total = int(total_pages)
        self.boundaries = int(boundaries)
        self.around = int(around)

    @staticmethod
    def _validate(**kwargs):
        for value in kwargs.values():
            if not((isinstance(value, int) or (isinstance(value, str) and value.isnumeric())) and int(value) >= 0):
                raise ValueError('Arguments must be either positive integer or zero')

        if not (kwargs['current'] and kwargs['total']):
            raise ValueError('"current_page" and "total_pages" cannot be zero')

        if kwargs['total'] < kwargs['current']:
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

        return [ELLIPSIS] + list(map(str, range(left_tail_edge+1, self.total+1)))

    def get_pages(self):
        left_body_edge, right_body_edge = self._get_body_edges()

        head = ' '.join(self._get_head(left_body_edge))
        tail = ' '.join(self._get_tail(right_body_edge))
        body = ' '.join(map(str, range(left_body_edge, right_body_edge+1)))

        return ' '.join(filter(None, [head, body, tail]))

    def print_pages(self):
        print(self.get_pages())


if __name__ == '__main__':
    args = input('Give me four numbers <current_page> <total_pages> <boundaries> <boundaries>: ').split()[:4]
    Paginator(*args).print_pages()
