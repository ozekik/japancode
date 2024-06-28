from japancode.utils import _hiragana_to_katakana, _load_data, lgcode_ensure_checkdigit


class Region:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    # def __repr__(self) -> str:
    #     # TODO: Fix this
    #     return f"Region({self.name})"

    def lgcode(self, checkdigit=True) -> str | None:
        """Return the local government code for a prefecture.

        Args:
            pref_name: The name of the prefecture.
            checkdigit: Whether to include the check digit. (Default: True)

        Returns:
            The local government code for the prefecture.

        >>> Region("東京都").lgcode()
        '130001'
        >>> Region("東京都").lgcode(checkdigit=False)
        '13000'
        """
        region_data = _load_data()

        match = next(filter(lambda x: x.name == self.name, region_data), None)

        if not match:
            return None

        _lgcode = match.lgcode
        _lgcode = lgcode_ensure_checkdigit(_lgcode)

        return _lgcode if checkdigit else _lgcode[:5]

    @classmethod
    def from_lgcode(cls, code: str, checkdigit=True):
        """Return the name of the prefecture for a local government code.

        Args:
            code: The local government code.
            checkdigit: Whether the code includes the check digit. (Default: True)

        Returns:
            The name of the prefecture for the local government code.

        >>> Region.from_lgcode("130001").name
        '東京都'
        """
        region_data = _load_data()

        match = next(
            filter(
                lambda x: x.lgcode == code if checkdigit else x.lgcode[:5] == code,
                region_data,
            ),
            None,
        )

        if not match:
            return None

        return cls(match.name)

    def roman(self, capitalize=False):
        """Return the romanized name of a region.

        Args:
            capitalize: Whether to capitalize the first letter of the romanized name.

        Returns:
            The romanized name of the region.

        >>> Region("東京都").roman()
        'tokyo'
        >>> Region("東京都").roman(capitalize=True)
        'Tokyo'
        """
        # TODO: Support -to, -do, -fu, -ken
        # TODO: Support overline, Hepburn, etc.

        region_data = _load_data()

        match = next(filter(lambda x: x.name == self.name, region_data), None)

        if not match:
            return None

        if capitalize:
            return match.roman
        else:
            if match.roman is None:
                return None
            else:
                return match.roman.lower()

    def kana(self, katakana=False):
        """Return the kana name of a region.

        Args:
            katakana: Whether to return the kana name in katakana.

        Returns:
            The kana name of the region.

        >>> Region("東京都").kana()
        'とうきょうと'
        >>> Region("東京都").kana(katakana=True)
        'トウキョウト'
        """
        region_data = _load_data()

        match = next(filter(lambda x: x.name == self.name, region_data), None)

        if not match:
            return None

        kana = match.kana

        if kana is not None and katakana:
            katakana = _hiragana_to_katakana(kana)
            return katakana
        else:
            return kana


class Prefecture(Region):
    def isocode(self):
        """Return the ISO 3166-2 code for a prefecture.

        Returns:
            The ISO 3166-2 code for the prefecture.

        >>> Prefecture("東京都").isocode()
        'JP-13'
        """
        region_data = _load_data()

        match = next(filter(lambda x: x.name == self.name, region_data), None)

        if not match:
            return None

        return match.isocode

    @classmethod
    def from_isocode(cls, isocode: str):
        """Return a prefecture object from an ISO 3166-2 code.

        Args:
            isocode: The ISO 3166-2 code for the prefecture.

        Returns:
            A Prefecture object.

        >>> Prefecture.from_isocode("JP-13").name
        '東京都'
        """

        region_data = _load_data()

        match = next(filter(lambda x: x.isocode == isocode, region_data), None)

        if not match:
            return None

        return cls(match.name)

    def jiscode(self) -> str | None:
        """Return the JIS X 0401 code for a prefecture.

        Returns:
            The JIS X 0401 code for the prefecture.

        >>> Prefecture("東京都").jiscode()
        '13'
        """
        region_data = _load_data()

        match = next(filter(lambda x: x.name == self.name, region_data), None)

        if not match or match.type != "prefectural":
            return None

        if (pid := match.pref_id) is not None:
            return pid.zfill(2)
        else:
            return None

    @classmethod
    def from_jiscode(cls, jiscode: str):
        """Return a prefecture object from a JIS X 0401 code.

        Args:
            jiscode: The JIS X 0401 code for the prefecture.

        Returns:
            A Prefecture object.

        >>> Prefecture.from_jiscode("13").name
        '東京都'
        """
        region_data = _load_data()

        match = next(filter(lambda x: x.pref_id.zfill(2) == jiscode, region_data), None)

        if not match:
            return None

        return cls(match.name)
