import math
from django.core.paginator import Paginator


def make_pagination_range(page_range, num_pages, current_page):
    middle_range = math.ceil(num_pages / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = page_range[start_range:stop_range]
    return {
        "pagination": pagination,
        "page_range": page_range,
        "total_pages": total_pages,
        "num_pages": num_pages,
        "current_page": current_page,
        "start_range": start_range,
        "stop_range": stop_range,
        "frist_page_out_of_range": current_page > middle_range,
        "last_page_out_of_range": stop_range < total_pages,
    }

def make_pagination(request, quary_set, num_obj: int, num_pages=4):
    try:
        current_page = int(request.GET.get('page', 1)) 
    except ValueError:
        current_page = 1

    paginator = Paginator(quary_set, num_obj)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        current_page=current_page,
        num_pages=num_pages,
        page_range=paginator.page_range
    )

    return page_obj, pagination_range