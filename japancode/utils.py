import json
from dataclasses import dataclass
from pathlib import Path

_region_data = None


@dataclass
class RegionData:
    type: str  # TODO: Enum: prefectural, municipal
    name: str
    kana: str
    roman: str | None
    isocode: str | None
    lgcode: str
    pref_id: str


def _load_data():
    global _region_data

    if _region_data is not None:
        return _region_data

    with open(Path(Path(__file__).parent, "data/prefectures.json"), "r") as f:
        _prefectures_data = json.load(f)
        _prefectures_data = [
            RegionData(
                type="prefectural",
                name=x["pref"],
                kana=x["prefkana"],
                roman=x["pref_en"],
                isocode=x.get("ISO3166-2", None),
                lgcode=x["lgcode"],
                pref_id=x["pid"],
            )
            for x in _prefectures_data
        ]

    with open(Path(Path(__file__).parent, "data/municipalities.json"), "r") as f:
        _municiplaities_data = json.load(f)
        _municiplaities_data = [
            RegionData(
                type="municipal",
                name=x["city"],
                kana=x["citykana"],
                roman=None,
                isocode=x.get("ISO3166-2", None),
                lgcode=x["lgcode"],
                pref_id=x["pid"],
            )
            for x in _municiplaities_data
        ]

    _region_data = _prefectures_data + _municiplaities_data

    return _region_data


def _hiragana_to_katakana(hiragana: str) -> str:
    return hiragana.translate(
        str.maketrans(
            "っぁぃぅぇぉゃゅょあいうえおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもやゆよらりるれろわゐゑをん",
            "ッァィゥェォャュョアイウエオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤユヨラリルレロワヰヱヲン",
        )
    )


def lgcode_ensure_checkdigit(lgcode: str):
    """Return the check digit for a local government code.

    Args:
        lgcode: The local government code.

    Returns:
        The check digit for the local government code.

    >>> lgcode_ensure_checkdigit("13000")
    '130001'

    >>> lgcode_ensure_checkdigit("13101")
    '131016'
    """
    if len(lgcode) == 6:
        return lgcode
    elif len(lgcode) != 5:
        raise ValueError("Local government code must be 5 or 6 digits long.")

    checkdigit = (
        11 - sum([int(lgcode[-(i + 1)]) * (i + 2) for i in range(5)]) % 11
    ) % 10

    return lgcode + str(checkdigit)
