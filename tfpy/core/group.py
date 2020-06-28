"""Define the group module."""


def correlate(groups_, users):
    """
    Correlate the role with the users via the groups.

    :param groups_ dict: dict mapping a group to a list of roles
    :param users dict: dict mapping a user to a list of groups
    :return dict: a dict mapping a role do a list of users.
    """
    d = {}
    for user, groups in users.items():
        for group in groups:
            roles = groups_.get(group, [])
            for role in roles:
                d.setdefault(role, []).append(user)

    return d
