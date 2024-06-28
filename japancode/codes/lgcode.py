from japancode.region import Region


def tocode(pref_name: str, checkdigit=True) -> str | None:
    """Return the local government code for a prefecture.

    Args:
        pref_name: The name of the prefecture.
        checkdigit: Whether to include the check digit. (Default: True)

    Returns:
        The local government code for the prefecture.

    >>> tocode("東京都")
    '130001'
    """
    return Region(pref_name).lgcode(checkdigit=checkdigit)


def reverse(code: str, checkdigit=True):
    """Return the name of the prefecture for a local government code.

    Args:
        code: The local government code.
        checkdigit: Whether the code includes the check digit. (Default: True)

    Returns:
        The Region object for the local government code.

    >>> reverse("130001").name
    '東京都'
    """
    return Region.from_lgcode(code, checkdigit=checkdigit)
