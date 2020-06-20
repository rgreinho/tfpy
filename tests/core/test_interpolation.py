"""Test the interpolation module."""
import pytest
from terraformpy import Module
from terraformpy import Variable

from tfpy.core import interpolation


def test_interpolate():
    """Ensure a resource is interpolated."""
    actual = interpolation.interpolate("resource", "name", "attribute")
    expected = "${resource.name.attribute}"
    assert actual == expected


def test_module_interpolate():
    """Ensure a module is interpolated."""
    actual = interpolation.m("name", "attribute")
    expected = "${module.name.attribute}"
    assert actual == expected


def test_variable_interpolate():
    """Ensure a variable is interpolated."""
    actual = interpolation.v("name")
    expected = "${var.name}"
    assert actual == expected


@pytest.mark.parametrize(
    "tfobject,args,representation",
    [
        pytest.param(
            Variable("variable_name"),
            [],
            "${var.variable_name}",
            id="interpolate-variable",
        ),
        pytest.param(
            Module("module_name"),
            ["attribute"],
            "${module.module_name.attribute}",
            id="interpolate-module",
        ),
    ],
)
def test_i(tfobject, args, representation):
    """Ensure a TF object is interpolated."""
    assert interpolation.i(tfobject, *args) == representation
