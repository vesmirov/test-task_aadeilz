class Paginator:
    def __init__(self, current=15, total=50, boundaries=4, around=5):
        self.current = current
        self.total = total
        self.boundaries = boundaries
        self.around = around

    def get_pages(self):
        pass


if __name__ == '__main__':
    paginator = Paginator()
    print(paginator.get_pages())
