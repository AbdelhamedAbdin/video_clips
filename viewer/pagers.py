def page_navigation(get_page, page_number) -> object:
    if get_page.has_next():
        next_url = f"?page={get_page.next_page_number()}"
    else:
        next_url = ''

    if get_page.has_previous():
        prev_url = f"?page={get_page.previous_page_number()}"
    else:
        prev_url = ''

    try:
        p = int(page_number)
    except TypeError:
        p = 0

    is_pager = True
    if p > get_page.number:
        is_pager = False

    return {
        'next_url': next_url,
        'prev_url': prev_url,
        'is_pager': is_pager
    }