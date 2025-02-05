def from_to(
    str,
    start_str,
    end_str,
):

    start_idx = str.find(start_str)
    end_idx = str.find(end_str)

    return str[start_idx + len(start_str):end_idx]
