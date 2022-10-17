class Paginator:
    def __init__(self, current_page, total_pages, boundaries=2, around=2):
        self._validate_arguments(
            current=current_page,
            total=total_pages,
            boundaries=boundaries,
            around=around
        )
        self.current = current_page
        self.total = total_pages
        self.boundaries = boundaries
        self.around = around

    @staticmethod
    def _validate_arguments(**kwargs):
        for value in kwargs.values():
            if not isinstance(value, int):
                raise ValueError('All arguments must be integers')
            elif value < 0:
                raise ValueError('Negative numbers are not allowed')

        if not (kwargs['current'] and kwargs['total']):
            raise ValueError('"current_page" and "total_pages" arguments must be greater that zero')

        if kwargs['total'] < kwargs['current']:
            raise ValueError('"total_page" cannot be lower than "current_page"')

    def _get_middle_edges(self):
        middle_edges = [self.current - self.around, self.current + self.around]

        if middle_edges[0] < 1:
            middle_edges[0] = 1

        if middle_edges[1] > self.total:
            middle_edges[1] = self.total

        return middle_edges

    def _get_leading_array(self, start_of_middle_array):
        if not self.boundaries:
            return '...' if start_of_middle_array > 1 else ''

        if self.boundaries >= start_of_middle_array - 1:
            return ' '.join(list(map(str, range(1, start_of_middle_array))))

        result = list(map(str, range(1, self.boundaries + 1))) + ['...']
        return ' '.join(result)

    def _get_closing_array(self, end_of_middle_edge):
        if not self.boundaries:
            return '...' if end_of_middle_edge < self.total else ''

        start_of_closing_array = self.total - self.boundaries
        if start_of_closing_array <= end_of_middle_edge:
            return ' '.join(list(map(str, range(end_of_middle_edge + 1, self.total + 1))))

        result = ['...'] + list(map(str, range(start_of_closing_array + 1, self.total + 1)))
        return ' '.join(result)

    def get_pages(self):
        middle_edge_start, middle_edge_end = self._get_middle_edges()

        leading_array = self._get_leading_array(middle_edge_start)
        closing_array = self._get_closing_array(middle_edge_end)
        middle_array = " ".join(map(str, range(middle_edge_start, middle_edge_end+1)))

        return ' '.join(filter(None, [leading_array, middle_array, closing_array]))


if __name__ == '__main__':
    paginator = Paginator()
    print(paginator.get_pages())
