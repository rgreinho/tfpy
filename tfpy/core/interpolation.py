"""
Define the module containing interpolation functions.

This module was created to mitigate the following TerrafomPy bugs:

* https://github.com/NerdWalletOSS/terraformpy/issues/65
* https://github.com/NerdWalletOSS/terraformpy/issues/66
"""
from terraformpy import Module
from terraformpy import Variable


def interpolate(resource, *args):
    """Return a string representing the reference to the resource."""
    return f"${{{resource}.{'.'.join(args)}}}"


def m(*args):
    """Interpolate a module."""
    return interpolate("module", *args)


def v(*args):
    """Interpolate a variable."""
    return interpolate("var", *args)


def i(tfobject, *args):
    """Interpolate a tfobject."""
    if isinstance(tfobject, Variable):
        return str(tfobject)
    if isinstance(tfobject, Module):
        return m(tfobject._name, *args)
    raise TypeError(f'resource "{tfobject}" is unsupported')
