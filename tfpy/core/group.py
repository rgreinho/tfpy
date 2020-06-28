"""Define the group module."""


def correlate(groups_, users):
    """
    Correlate the role with the users via the groups.

    Example:
        >>> # Define the groups and their roles.
        >>> groups = {
        >>>     "admin": ["role/owner", "role/manager"],
        >>>      "dev": ["role/viewer"],
        >>>      "ops": ["role/editor"],
        >>> }
        >>> # Define the users and their groups.
        >>> users = {
        >>>     "admin1": ["admin"],
        >>>     "admin2": ["admin"],
        >>>     "dev1": ["dev"],
        >>>     "dev2": ["dev"],
        >>>     "ops1": ["dev", "ops",],
        >>> }
        >>> result = {
        >>>     'role/owner': ['admin1', 'admin2'],
        >>>     'role/manager': ['admin1', 'admin2'],
        >>>     'role/viewer': ['dev1', 'dev2', 'ops1'],
        >>>     'role/editor': ['ops1']
        >>> }
        >>> assert correlate(groups, users) == result

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
