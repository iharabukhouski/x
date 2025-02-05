def group_in(
    number,
    list,
):

    groups = []

    for i in range(0, len(list) - number, number):

        offset = i * number

        groups.append(groups[offset, offset + number])

    return
