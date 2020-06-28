"""
Define the module containing interpolation functions.

This module was created to mitigate the following TerrafomPy bugs:

* https://github.com/NerdWalletOSS/terraformpy/issues/65
* https://github.com/NerdWalletOSS/terraformpy/issues/66
"""
from terraformpy import Module
from terraformpy import Variable


def interpolate(resource, *args):
    """
    Return a string representing the resource.

    Example:
        >>> interpolate("var", "region")
        ${var.region}
        >>> interpolate("module", "vpc", "network")
        ${module.vpc.network}

    :param resource str: resource name
    :param args list(str): a list of strings representing the Variable
        attributes to interpolate.
    :return str: a string representation of the resource and its arguments if
        any.
    """
    return f"${{{resource}.{'.'.join(args)}}}"


def m(*args):
    """
    Interpolate a module.

    Example:
        >>> m("vpc", "network")
        ${module.vpc.network}

    :param args list(str): a list of strings representing the Module
        attributes to interpolate.
    :return str: a string representation of the Variable and its arguments if
        any.
    """
    return interpolate("module", *args)


def v(*args):
    """
    Interpolate a variable.

    Example:
        >>> v("region")
        ${var.region}

    :param args list(str): a list of strings representing the Variable
        attributes to interpolate.
    :return str: a string representation of the Variable and its arguments if
        any.
    """
    return interpolate("var", *args)


def i(tfobject, *args):
    """
    Interpolate a tfobject.

    Example:
        >>> from terraformpy import Module
        >>> from terraformpy import Variable
        >>> v = Variable("region")
        >>> i(v)
        ${var.region}
        >>> m = Module("vpc")
        >>> i(m, "network")
         ${module.vpc.network}


    :param tfobject TFObject: terroformpy object to interpolate
    :param args list(str): a list of strings representing the TFObject
        attributes to interpolate.
    :return str: a string representation of the TFObject and its arguments if any.
    """
    if isinstance(tfobject, Variable):
        return str(tfobject)
    if isinstance(tfobject, Module):
        return m(tfobject._name, *args)
    raise TypeError(f'resource "{tfobject}" is unsupported')
