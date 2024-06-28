from japancode.region import Prefecture


def tocode(pref_name: str) -> str | None:
    """Return the JIS X 0401 code for a prefecture.

    Args:
        pref_name: The name of the prefecture.

    Returns:
        The JIS X 0401 code for the prefecture.

    >>> tocode("東京都")
    '13'
    """
    return Prefecture(pref_name).jiscode()


def reverse(code: str) -> Prefecture | None:
    """Return the name of the prefecture for a local government code.

    Args:
        code: The local government code.

    Returns:
        The name of the prefecture for the local government code.

    >>> reverse("13").name
    '東京都'
    """
    return Prefecture.from_jiscode(code)
