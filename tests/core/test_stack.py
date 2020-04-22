"""Test the stack module."""

from faker import Faker
import pytest
import yaml

from tfpy.core import stack

# Setup faker object.
fake = Faker()

CONFIG_STRING = """
common:
    testkey: "test value"
"""


@pytest.fixture
def stackvar():
    """Setup a stackvars object."""
    s = stack.StackVars(fake.word())
    s.vars = yaml.safe_load(CONFIG_STRING)
    return s


class TestStackvar:
    """Test the StackVar object."""

    def test_key_lookup_00(self, stackvar):
        """Ensure an existing key is found."""
        actual = stackvar.get("common.testkey")
        assert actual == "test value"

    def test_key_lookup_01(self, stackvar):
        """Ensure a missing key lookup raises an exception."""
        with pytest.raises(LookupError):
            stackvar.get("common.missingkey")

    def test_key_lookup_02(self, stackvar):
        """Ensure a missing key lookup returns the provided default value."""
        actual = stackvar.get("common:missingkey", "missing value")
        assert actual == "missing value"
