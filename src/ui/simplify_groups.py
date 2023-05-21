def simplify_groups(groups: list[str]):
    try:
        groups_ints = [int(group) for group in groups]
        groups_ints.sort()
        wanted_group = groups_ints[0]
        for group_int in groups_ints:
            if group_int != wanted_group:
                return False
            wanted_group += 1
        return groups_ints[0], wanted_group-1
    except ValueError:
        return False


if __name__ == "__main__":
    print(simplify_groups(['1', 'grupa2', '3', '4', '5', '6', '7', '8', '9', '10']))
