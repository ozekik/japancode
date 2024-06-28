from japancode.region import Prefecture


def tocode(pref_name: str) -> str | None:
    """Return the ISO 3166-2 code for a prefecture.

    Args:
        pref_name: The name of the prefecture.
        reverse: Whether to return the prefecture name from the ISO 3166-2 code.

    Returns:
        The ISO 3166-2 code for the prefecture.

    >>> tocode("東京都")
    'JP-13'
    """
    return Prefecture(pref_name).isocode()


def reverse(code: str) -> Prefecture | None:
    """Return the name of the prefecture for a ISO 3166-2 code.

    Args:
        code: The ISO 3166-2 code.

    Returns:
        The Prefecture object for the ISO 3166-2 code.

    >>> reverse("JP-13").name
    '東京都'
    """
    return Prefecture.from_isocode(code)
