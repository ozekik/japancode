from japancode.region import Region


def roman(pref_name: str, capitalize=False) -> str | None:
    """Return the romanized name of a prefecture.

    Args:
        pref_name: The name of the prefecture.
        capitalize: Whether to capitalize the first letter of the romanized name. (Default: False)

    Returns:
        The romanized name of the prefecture.

    >>> roman("東京都")
    'tokyo'
    >>> roman("東京都", capitalize=True)
    'Tokyo'
    """
    return Region(pref_name).roman(capitalize=capitalize)


def kana(pref_name: str, katakana=False) -> str | None:
    """Return the kana name of a prefecture.

    Args:
        pref_name: The name of the prefecture.
        katakana: Whether to return the kana name in katakana.

    Returns:
        The kana name of the prefecture.

    >>> kana("東京都")
    'とうきょうと'
    >>> kana("東京都", katakana=True)
    'トウキョウト'

    """
    return Region(pref_name).kana(katakana=katakana)
