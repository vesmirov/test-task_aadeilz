# Paginator

### Description
Paginator representation for web pages.  
Based on the specified parameters, demonstrate how the pagination will look.  
Requires such parameters as: current active page, total amount of pages,  
how many pages to display around the paginator edges, how many pages  
should be displayed around the active page.


### Usage
To use, you can import a class from a module and call one of the methods  
of the exposed interface. An alternative option is to run the python module  
directly.

#### First option:
```
from pagination import Paginator

kwargs = {'current_page': 4, 'total_pages': 10, 'boundaries': 2, 'around': 2}
pages = Paginator.get_pages(**kwargs)
print(pages)

...

Paginator.print_pages(**kwargs)
```

> 1 2 3 4 5 6 ... 9 10  
> 1 2 3 4 5 6 ... 9 10

#### Second option:
`$ ./pagination.py`
> Give me four numbers <current_page> <total_pages> <boundaries> <boundaries>: 4 10 2 2

> 1 2 3 4 5 6 ... 9 10
