"""Test the group module."""
from tfpy.core import group

GROUPS = {
    "admin": ["role/owner", "role/manager"],
    "dev": ["role/viewer"],
    "ops": ["role/editor"],
}

USERS = {
    "admin1": ["admin"],
    "admin2": ["admin"],
    "dev1": ["dev"],
    "dev2": ["dev"],
    "ops1": ["dev", "ops",],
}

USER_GROUPS_EXPANDED = {
    "role/editor": ["ops1"],
    "role/manager": ["admin1", "admin2"],
    "role/owner": ["admin1", "admin2"],
    "role/viewer": ["dev1", "dev2", "ops1"],
}


def test_manage_users_00():
    """Ensure a correct list of users is rendered correctly."""
    actual = group.correlate(GROUPS, USERS)
    expected = USER_GROUPS_EXPANDED
    assert actual == expected
