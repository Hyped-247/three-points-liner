def format_line_str(tup: tuple) -> str:
    """
    Format a line.
    :param tup: bool, number, number
    :return: str
    """
    if tup[0]:
        return f"x = {tup[1]}"

    return f"y = {tup[1]}x + {tup[2]}"
