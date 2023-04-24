from dataclasses import dataclass


class CountryNotFoundError(Exception):
    ...


@dataclass
class CountryData:
    name: str
    title: str
    emoji: str
    unicode: str


@dataclass
class Country:

    @classmethod
    def get(cls, code: str) -> 'CountryData':
        """
        Get a country data from the given code.

        :param code: country code in ISO 3166 format
        :return: :class:`CountryData`
        """

        try:
            return CountryData(**cls.data[code])

        except KeyError:
            raise CountryNotFoundError(
                f"Country code {code} not found."
            )

    @classmethod
    def get_emoji(cls, code: str) -> str:
        """
        Get a country emoji from the given code.

        :param code: country code in ISO 3166 format
        :return: :class:`CountryData`
        """
        return cls.get(code).emoji

    data = {
        "AD": {
            "emoji": "🇦🇩",
            "unicode": "U+1F1E6 U+1F1E9",
            "name": "Andorra",
            "title": "flag for Andorra"
        },
        "AE": {
            "emoji": "🇦🇪",
            "unicode": "U+1F1E6 U+1F1EA",
            "name": "United Arab Emirates",
            "title": "flag for United Arab Emirates"
        },
        "AF": {
            "emoji": "🇦🇫",
            "unicode": "U+1F1E6 U+1F1EB",
            "name": "Afghanistan",
            "title": "flag for Afghanistan"
        },
        "AG": {
            "emoji": "🇦🇬",
            "unicode": "U+1F1E6 U+1F1EC",
            "name": "Antigua and Barbuda",
            "title": "flag for Antigua and Barbuda"
        },
        "AI": {
            "emoji": "🇦🇮",
            "unicode": "U+1F1E6 U+1F1EE",
            "name": "Anguilla",
            "title": "flag for Anguilla"
        },
        "AL": {
            "emoji": "🇦🇱",
            "unicode": "U+1F1E6 U+1F1F1",
            "name": "Albania",
            "title": "flag for Albania"
        },
        "AM": {
            "emoji": "🇦🇲",
            "unicode": "U+1F1E6 U+1F1F2",
            "name": "Armenia",
            "title": "flag for Armenia"
        },
        "AO": {
            "emoji": "🇦🇴",
            "unicode": "U+1F1E6 U+1F1F4",
            "name": "Angola",
            "title": "flag for Angola"
        },
        "AQ": {
            "emoji": "🇦🇶",
            "unicode": "U+1F1E6 U+1F1F6",
            "name": "Antarctica",
            "title": "flag for Antarctica"
        },
        "AR": {
            "emoji": "🇦🇷",
            "unicode": "U+1F1E6 U+1F1F7",
            "name": "Argentina",
            "title": "flag for Argentina"
        },
        "AS": {
            "emoji": "🇦🇸",
            "unicode": "U+1F1E6 U+1F1F8",
            "name": "American Samoa",
            "title": "flag for American Samoa"
        },
        "AT": {
            "emoji": "🇦🇹",
            "unicode": "U+1F1E6 U+1F1F9",
            "name": "Austria",
            "title": "flag for Austria"
        },
        "AU": {
            "emoji": "🇦🇺",
            "unicode": "U+1F1E6 U+1F1FA",
            "name": "Australia",
            "title": "flag for Australia"
        },
        "AW": {
            "emoji": "🇦🇼",
            "unicode": "U+1F1E6 U+1F1FC",
            "name": "Aruba",
            "title": "flag for Aruba"
        },
        "AX": {
            "emoji": "🇦🇽",
            "unicode": "U+1F1E6 U+1F1FD",
            "name": "Åland Islands",
            "title": "flag for Åland Islands"
        },
        "AZ": {
            "emoji": "🇦🇿",
            "unicode": "U+1F1E6 U+1F1FF",
            "name": "Azerbaijan",
            "title": "flag for Azerbaijan"
        },
        "BA": {
            "emoji": "🇧🇦",
            "unicode": "U+1F1E7 U+1F1E6",
            "name": "Bosnia and Herzegovina",
            "title": "flag for Bosnia and Herzegovina"
        },
        "BB": {
            "emoji": "🇧🇧",
            "unicode": "U+1F1E7 U+1F1E7",
            "name": "Barbados",
            "title": "flag for Barbados"
        },
        "BD": {
            "emoji": "🇧🇩",
            "unicode": "U+1F1E7 U+1F1E9",
            "name": "Bangladesh",
            "title": "flag for Bangladesh"
        },
        "BE": {
            "emoji": "🇧🇪",
            "unicode": "U+1F1E7 U+1F1EA",
            "name": "Belgium",
            "title": "flag for Belgium"
        },
        "BF": {
            "emoji": "🇧🇫",
            "unicode": "U+1F1E7 U+1F1EB",
            "name": "Burkina Faso",
            "title": "flag for Burkina Faso"
        },
        "BG": {
            "emoji": "🇧🇬",
            "unicode": "U+1F1E7 U+1F1EC",
            "name": "Bulgaria",
            "title": "flag for Bulgaria"
        },
        "BH": {
            "emoji": "🇧🇭",
            "unicode": "U+1F1E7 U+1F1ED",
            "name": "Bahrain",
            "title": "flag for Bahrain"
        },
        "BI": {
            "emoji": "🇧🇮",
            "unicode": "U+1F1E7 U+1F1EE",
            "name": "Burundi",
            "title": "flag for Burundi"
        },
        "BJ": {
            "emoji": "🇧🇯",
            "unicode": "U+1F1E7 U+1F1EF",
            "name": "Benin",
            "title": "flag for Benin"
        },
        "BL": {
            "emoji": "🇧🇱",
            "unicode": "U+1F1E7 U+1F1F1",
            "name": "Saint Barthélemy",
            "title": "flag for Saint Barthélemy"
        },
        "BM": {
            "emoji": "🇧🇲",
            "unicode": "U+1F1E7 U+1F1F2",
            "name": "Bermuda",
            "title": "flag for Bermuda"
        },
        "BN": {
            "emoji": "🇧🇳",
            "unicode": "U+1F1E7 U+1F1F3",
            "name": "Brunei Darussalam",
            "title": "flag for Brunei Darussalam"
        },
        "BO": {
            "emoji": "🇧🇴",
            "unicode": "U+1F1E7 U+1F1F4",
            "name": "Bolivia",
            "title": "flag for Bolivia"
        },
        "BQ": {
            "emoji": "🇧🇶",
            "unicode": "U+1F1E7 U+1F1F6",
            "name": "Bonaire, Sint Eustatius and Saba",
            "title": "flag for Bonaire, Sint Eustatius and Saba"
        },
        "BR": {
            "emoji": "🇧🇷",
            "unicode": "U+1F1E7 U+1F1F7",
            "name": "Brazil",
            "title": "flag for Brazil"
        },
        "BS": {
            "emoji": "🇧🇸",
            "unicode": "U+1F1E7 U+1F1F8",
            "name": "Bahamas",
            "title": "flag for Bahamas"
        },
        "BT": {
            "emoji": "🇧🇹",
            "unicode": "U+1F1E7 U+1F1F9",
            "name": "Bhutan",
            "title": "flag for Bhutan"
        },
        "BV": {
            "emoji": "🇧🇻",
            "unicode": "U+1F1E7 U+1F1FB",
            "name": "Bouvet Island",
            "title": "flag for Bouvet Island"
        },
        "BW": {
            "emoji": "🇧🇼",
            "unicode": "U+1F1E7 U+1F1FC",
            "name": "Botswana",
            "title": "flag for Botswana"
        },
        "BY": {
            "emoji": "🇧🇾",
            "unicode": "U+1F1E7 U+1F1FE",
            "name": "Belarus",
            "title": "flag for Belarus"
        },
        "BZ": {
            "emoji": "🇧🇿",
            "unicode": "U+1F1E7 U+1F1FF",
            "name": "Belize",
            "title": "flag for Belize"
        },
        "CA": {
            "emoji": "🇨🇦",
            "unicode": "U+1F1E8 U+1F1E6",
            "name": "Canada",
            "title": "flag for Canada"
        },
        "CC": {
            "emoji": "🇨🇨",
            "unicode": "U+1F1E8 U+1F1E8",
            "name": "Cocos (Keeling) Islands",
            "title": "flag for Cocos (Keeling) Islands"
        },
        "CD": {
            "emoji": "🇨🇩",
            "unicode": "U+1F1E8 U+1F1E9",
            "name": "Congo",
            "title": "flag for Congo"
        },
        "CF": {
            "emoji": "🇨🇫",
            "unicode": "U+1F1E8 U+1F1EB",
            "name": "Central African Republic",
            "title": "flag for Central African Republic"
        },
        "CG": {
            "emoji": "🇨🇬",
            "unicode": "U+1F1E8 U+1F1EC",
            "name": "Congo",
            "title": "flag for Congo"
        },
        "CH": {
            "emoji": "🇨🇭",
            "unicode": "U+1F1E8 U+1F1ED",
            "name": "Switzerland",
            "title": "flag for Switzerland"
        },
        "CI": {
            "emoji": "🇨🇮",
            "unicode": "U+1F1E8 U+1F1EE",
            "name": "Côte D'Ivoire",
            "title": "flag for Côte D'Ivoire"
        },
        "CK": {
            "emoji": "🇨🇰",
            "unicode": "U+1F1E8 U+1F1F0",
            "name": "Cook Islands",
            "title": "flag for Cook Islands"
        },
        "CL": {
            "emoji": "🇨🇱",
            "unicode": "U+1F1E8 U+1F1F1",
            "name": "Chile",
            "title": "flag for Chile"
        },
        "CM": {
            "emoji": "🇨🇲",
            "unicode": "U+1F1E8 U+1F1F2",
            "name": "Cameroon",
            "title": "flag for Cameroon"
        },
        "CN": {
            "emoji": "🇨🇳",
            "unicode": "U+1F1E8 U+1F1F3",
            "name": "China",
            "title": "flag for China"
        },
        "CO": {
            "emoji": "🇨🇴",
            "unicode": "U+1F1E8 U+1F1F4",
            "name": "Colombia",
            "title": "flag for Colombia"
        },
        "CR": {
            "emoji": "🇨🇷",
            "unicode": "U+1F1E8 U+1F1F7",
            "name": "Costa Rica",
            "title": "flag for Costa Rica"
        },
        "CU": {
            "emoji": "🇨🇺",
            "unicode": "U+1F1E8 U+1F1FA",
            "name": "Cuba",
            "title": "flag for Cuba"
        },
        "CV": {
            "emoji": "🇨🇻",
            "unicode": "U+1F1E8 U+1F1FB",
            "name": "Cape Verde",
            "title": "flag for Cape Verde"
        },
        "CW": {
            "emoji": "🇨🇼",
            "unicode": "U+1F1E8 U+1F1FC",
            "name": "Curaçao",
            "title": "flag for Curaçao"
        },
        "CX": {
            "emoji": "🇨🇽",
            "unicode": "U+1F1E8 U+1F1FD",
            "name": "Christmas Island",
            "title": "flag for Christmas Island"
        },
        "CY": {
            "emoji": "🇨🇾",
            "unicode": "U+1F1E8 U+1F1FE",
            "name": "Cyprus",
            "title": "flag for Cyprus"
        },
        "CZ": {
            "emoji": "🇨🇿",
            "unicode": "U+1F1E8 U+1F1FF",
            "name": "Czech Republic",
            "title": "flag for Czech Republic"
        },
        "DE": {
            "emoji": "🇩🇪",
            "unicode": "U+1F1E9 U+1F1EA",
            "name": "Germany",
            "title": "flag for Germany"
        },
        "DJ": {
            "emoji": "🇩🇯",
            "unicode": "U+1F1E9 U+1F1EF",
            "name": "Djibouti",
            "title": "flag for Djibouti"
        },
        "DK": {
            "emoji": "🇩🇰",
            "unicode": "U+1F1E9 U+1F1F0",
            "name": "Denmark",
            "title": "flag for Denmark"
        },
        "DM": {
            "emoji": "🇩🇲",
            "unicode": "U+1F1E9 U+1F1F2",
            "name": "Dominica",
            "title": "flag for Dominica"
        },
        "DO": {
            "emoji": "🇩🇴",
            "unicode": "U+1F1E9 U+1F1F4",
            "name": "Dominican Republic",
            "title": "flag for Dominican Republic"
        },
        "DZ": {
            "emoji": "🇩🇿",
            "unicode": "U+1F1E9 U+1F1FF",
            "name": "Algeria",
            "title": "flag for Algeria"
        },
        "EC": {
            "emoji": "🇪🇨",
            "unicode": "U+1F1EA U+1F1E8",
            "name": "Ecuador",
            "title": "flag for Ecuador"
        },
        "EE": {
            "emoji": "🇪🇪",
            "unicode": "U+1F1EA U+1F1EA",
            "name": "Estonia",
            "title": "flag for Estonia"
        },
        "EG": {
            "emoji": "🇪🇬",
            "unicode": "U+1F1EA U+1F1EC",
            "name": "Egypt",
            "title": "flag for Egypt"
        },
        "EH": {
            "emoji": "🇪🇭",
            "unicode": "U+1F1EA U+1F1ED",
            "name": "Western Sahara",
            "title": "flag for Western Sahara"
        },
        "ER": {
            "emoji": "🇪🇷",
            "unicode": "U+1F1EA U+1F1F7",
            "name": "Eritrea",
            "title": "flag for Eritrea"
        },
        "ES": {
            "emoji": "🇪🇸",
            "unicode": "U+1F1EA U+1F1F8",
            "name": "Spain",
            "title": "flag for Spain"
        },
        "ET": {
            "emoji": "🇪🇹",
            "unicode": "U+1F1EA U+1F1F9",
            "name": "Ethiopia",
            "title": "flag for Ethiopia"
        },
        "EU": {
            "emoji": "🇪🇺",
            "unicode": "U+1F1EA U+1F1FA",
            "name": "European Union",
            "title": "flag for European Union"
        },
        "FI": {
            "emoji": "🇫🇮",
            "unicode": "U+1F1EB U+1F1EE",
            "name": "Finland",
            "title": "flag for Finland"
        },
        "FJ": {
            "emoji": "🇫🇯",
            "unicode": "U+1F1EB U+1F1EF",
            "name": "Fiji",
            "title": "flag for Fiji"
        },
        "FK": {
            "emoji": "🇫🇰",
            "unicode": "U+1F1EB U+1F1F0",
            "name": "Falkland Islands (Malvinas)",
            "title": "flag for Falkland Islands (Malvinas)"
        },
        "FM": {
            "emoji": "🇫🇲",
            "unicode": "U+1F1EB U+1F1F2",
            "name": "Micronesia",
            "title": "flag for Micronesia"
        },
        "FO": {
            "emoji": "🇫🇴",
            "unicode": "U+1F1EB U+1F1F4",
            "name": "Faroe Islands",
            "title": "flag for Faroe Islands"
        },
        "FR": {
            "emoji": "🇫🇷",
            "unicode": "U+1F1EB U+1F1F7",
            "name": "France",
            "title": "flag for France"
        },
        "GA": {
            "emoji": "🇬🇦",
            "unicode": "U+1F1EC U+1F1E6",
            "name": "Gabon",
            "title": "flag for Gabon"
        },
        "GB": {
            "emoji": "🇬🇧",
            "unicode": "U+1F1EC U+1F1E7",
            "name": "United Kingdom",
            "title": "flag for United Kingdom"
        },
        "GD": {
            "emoji": "🇬🇩",
            "unicode": "U+1F1EC U+1F1E9",
            "name": "Grenada",
            "title": "flag for Grenada"
        },
        "GE": {
            "emoji": "🇬🇪",
            "unicode": "U+1F1EC U+1F1EA",
            "name": "Georgia",
            "title": "flag for Georgia"
        },
        "GF": {
            "emoji": "🇬🇫",
            "unicode": "U+1F1EC U+1F1EB",
            "name": "French Guiana",
            "title": "flag for French Guiana"
        },
        "GG": {
            "emoji": "🇬🇬",
            "unicode": "U+1F1EC U+1F1EC",
            "name": "Guernsey",
            "title": "flag for Guernsey"
        },
        "GH": {
            "emoji": "🇬🇭",
            "unicode": "U+1F1EC U+1F1ED",
            "name": "Ghana",
            "title": "flag for Ghana"
        },
        "GI": {
            "emoji": "🇬🇮",
            "unicode": "U+1F1EC U+1F1EE",
            "name": "Gibraltar",
            "title": "flag for Gibraltar"
        },
        "GL": {
            "emoji": "🇬🇱",
            "unicode": "U+1F1EC U+1F1F1",
            "name": "Greenland",
            "title": "flag for Greenland"
        },
        "GM": {
            "emoji": "🇬🇲",
            "unicode": "U+1F1EC U+1F1F2",
            "name": "Gambia",
            "title": "flag for Gambia"
        },
        "GN": {
            "emoji": "🇬🇳",
            "unicode": "U+1F1EC U+1F1F3",
            "name": "Guinea",
            "title": "flag for Guinea"
        },
        "GP": {
            "emoji": "🇬🇵",
            "unicode": "U+1F1EC U+1F1F5",
            "name": "Guadeloupe",
            "title": "flag for Guadeloupe"
        },
        "GQ": {
            "emoji": "🇬🇶",
            "unicode": "U+1F1EC U+1F1F6",
            "name": "Equatorial Guinea",
            "title": "flag for Equatorial Guinea"
        },
        "GR": {
            "emoji": "🇬🇷",
            "unicode": "U+1F1EC U+1F1F7",
            "name": "Greece",
            "title": "flag for Greece"
        },
        "GS": {
            "emoji": "🇬🇸",
            "unicode": "U+1F1EC U+1F1F8",
            "name": "South Georgia",
            "title": "flag for South Georgia"
        },
        "GT": {
            "emoji": "🇬🇹",
            "unicode": "U+1F1EC U+1F1F9",
            "name": "Guatemala",
            "title": "flag for Guatemala"
        },
        "GU": {
            "emoji": "🇬🇺",
            "unicode": "U+1F1EC U+1F1FA",
            "name": "Guam",
            "title": "flag for Guam"
        },
        "GW": {
            "emoji": "🇬🇼",
            "unicode": "U+1F1EC U+1F1FC",
            "name": "Guinea-Bissau",
            "title": "flag for Guinea-Bissau"
        },
        "GY": {
            "emoji": "🇬🇾",
            "unicode": "U+1F1EC U+1F1FE",
            "name": "Guyana",
            "title": "flag for Guyana"
        },
        "HK": {
            "emoji": "🇭🇰",
            "unicode": "U+1F1ED U+1F1F0",
            "name": "Hong Kong",
            "title": "flag for Hong Kong"
        },
        "HM": {
            "emoji": "🇭🇲",
            "unicode": "U+1F1ED U+1F1F2",
            "name": "Heard Island and Mcdonald Islands",
            "title": "flag for Heard Island and Mcdonald Islands"
        },
        "HN": {
            "emoji": "🇭🇳",
            "unicode": "U+1F1ED U+1F1F3",
            "name": "Honduras",
            "title": "flag for Honduras"
        },
        "HR": {
            "emoji": "🇭🇷",
            "unicode": "U+1F1ED U+1F1F7",
            "name": "Croatia",
            "title": "flag for Croatia"
        },
        "HT": {
            "emoji": "🇭🇹",
            "unicode": "U+1F1ED U+1F1F9",
            "name": "Haiti",
            "title": "flag for Haiti"
        },
        "HU": {
            "emoji": "🇭🇺",
            "unicode": "U+1F1ED U+1F1FA",
            "name": "Hungary",
            "title": "flag for Hungary"
        },
        "ID": {
            "emoji": "🇮🇩",
            "unicode": "U+1F1EE U+1F1E9",
            "name": "Indonesia",
            "title": "flag for Indonesia"
        },
        "IE": {
            "emoji": "🇮🇪",
            "unicode": "U+1F1EE U+1F1EA",
            "name": "Ireland",
            "title": "flag for Ireland"
        },
        "IL": {
            "emoji": "🇮🇱",
            "unicode": "U+1F1EE U+1F1F1",
            "name": "Israel",
            "title": "flag for Israel"
        },
        "IM": {
            "emoji": "🇮🇲",
            "unicode": "U+1F1EE U+1F1F2",
            "name": "Isle of Man",
            "title": "flag for Isle of Man"
        },
        "IN": {
            "emoji": "🇮🇳",
            "unicode": "U+1F1EE U+1F1F3",
            "name": "India",
            "title": "flag for India"
        },
        "IO": {
            "emoji": "🇮🇴",
            "unicode": "U+1F1EE U+1F1F4",
            "name": "British Indian Ocean Territory",
            "title": "flag for British Indian Ocean Territory"
        },
        "IQ": {
            "emoji": "🇮🇶",
            "unicode": "U+1F1EE U+1F1F6",
            "name": "Iraq",
            "title": "flag for Iraq"
        },
        "IR": {
            "emoji": "🇮🇷",
            "unicode": "U+1F1EE U+1F1F7",
            "name": "Iran",
            "title": "flag for Iran"
        },
        "IS": {
            "emoji": "🇮🇸",
            "unicode": "U+1F1EE U+1F1F8",
            "name": "Iceland",
            "title": "flag for Iceland"
        },
        "IT": {
            "emoji": "🇮🇹",
            "unicode": "U+1F1EE U+1F1F9",
            "name": "Italy",
            "title": "flag for Italy"
        },
        "JE": {
            "emoji": "🇯🇪",
            "unicode": "U+1F1EF U+1F1EA",
            "name": "Jersey",
            "title": "flag for Jersey"
        },
        "JM": {
            "emoji": "🇯🇲",
            "unicode": "U+1F1EF U+1F1F2",
            "name": "Jamaica",
            "title": "flag for Jamaica"
        },
        "JO": {
            "emoji": "🇯🇴",
            "unicode": "U+1F1EF U+1F1F4",
            "name": "Jordan",
            "title": "flag for Jordan"
        },
        "JP": {
            "emoji": "🇯🇵",
            "unicode": "U+1F1EF U+1F1F5",
            "name": "Japan",
            "title": "flag for Japan"
        },
        "KE": {
            "emoji": "🇰🇪",
            "unicode": "U+1F1F0 U+1F1EA",
            "name": "Kenya",
            "title": "flag for Kenya"
        },
        "KG": {
            "emoji": "🇰🇬",
            "unicode": "U+1F1F0 U+1F1EC",
            "name": "Kyrgyzstan",
            "title": "flag for Kyrgyzstan"
        },
        "KH": {
            "emoji": "🇰🇭",
            "unicode": "U+1F1F0 U+1F1ED",
            "name": "Cambodia",
            "title": "flag for Cambodia"
        },
        "KI": {
            "emoji": "🇰🇮",
            "unicode": "U+1F1F0 U+1F1EE",
            "name": "Kiribati",
            "title": "flag for Kiribati"
        },
        "KM": {
            "emoji": "🇰🇲",
            "unicode": "U+1F1F0 U+1F1F2",
            "name": "Comoros",
            "title": "flag for Comoros"
        },
        "KN": {
            "emoji": "🇰🇳",
            "unicode": "U+1F1F0 U+1F1F3",
            "name": "Saint Kitts and Nevis",
            "title": "flag for Saint Kitts and Nevis"
        },
        "KP": {
            "emoji": "🇰🇵",
            "unicode": "U+1F1F0 U+1F1F5",
            "name": "North Korea",
            "title": "flag for North Korea"
        },
        "KR": {
            "emoji": "🇰🇷",
            "unicode": "U+1F1F0 U+1F1F7",
            "name": "South Korea",
            "title": "flag for South Korea"
        },
        "KW": {
            "emoji": "🇰🇼",
            "unicode": "U+1F1F0 U+1F1FC",
            "name": "Kuwait",
            "title": "flag for Kuwait"
        },
        "KY": {
            "emoji": "🇰🇾",
            "unicode": "U+1F1F0 U+1F1FE",
            "name": "Cayman Islands",
            "title": "flag for Cayman Islands"
        },
        "KZ": {
            "emoji": "🇰🇿",
            "unicode": "U+1F1F0 U+1F1FF",
            "name": "Kazakhstan",
            "title": "flag for Kazakhstan"
        },
        "LA": {
            "emoji": "🇱🇦",
            "unicode": "U+1F1F1 U+1F1E6",
            "name": "Lao People's Democratic Republic",
            "title": "flag for Lao People's Democratic Republic"
        },
        "LB": {
            "emoji": "🇱🇧",
            "unicode": "U+1F1F1 U+1F1E7",
            "name": "Lebanon",
            "title": "flag for Lebanon"
        },
        "LC": {
            "emoji": "🇱🇨",
            "unicode": "U+1F1F1 U+1F1E8",
            "name": "Saint Lucia",
            "title": "flag for Saint Lucia"
        },
        "LI": {
            "emoji": "🇱🇮",
            "unicode": "U+1F1F1 U+1F1EE",
            "name": "Liechtenstein",
            "title": "flag for Liechtenstein"
        },
        "LK": {
            "emoji": "🇱🇰",
            "unicode": "U+1F1F1 U+1F1F0",
            "name": "Sri Lanka",
            "title": "flag for Sri Lanka"
        },
        "LR": {
            "emoji": "🇱🇷",
            "unicode": "U+1F1F1 U+1F1F7",
            "name": "Liberia",
            "title": "flag for Liberia"
        },
        "LS": {
            "emoji": "🇱🇸",
            "unicode": "U+1F1F1 U+1F1F8",
            "name": "Lesotho",
            "title": "flag for Lesotho"
        },
        "LT": {
            "emoji": "🇱🇹",
            "unicode": "U+1F1F1 U+1F1F9",
            "name": "Lithuania",
            "title": "flag for Lithuania"
        },
        "LU": {
            "emoji": "🇱🇺",
            "unicode": "U+1F1F1 U+1F1FA",
            "name": "Luxembourg",
            "title": "flag for Luxembourg"
        },
        "LV": {
            "emoji": "🇱🇻",
            "unicode": "U+1F1F1 U+1F1FB",
            "name": "Latvia",
            "title": "flag for Latvia"
        },
        "LY": {
            "emoji": "🇱🇾",
            "unicode": "U+1F1F1 U+1F1FE",
            "name": "Libya",
            "title": "flag for Libya"
        },
        "MA": {
            "emoji": "🇲🇦",
            "unicode": "U+1F1F2 U+1F1E6",
            "name": "Morocco",
            "title": "flag for Morocco"
        },
        "MC": {
            "emoji": "🇲🇨",
            "unicode": "U+1F1F2 U+1F1E8",
            "name": "Monaco",
            "title": "flag for Monaco"
        },
        "MD": {
            "emoji": "🇲🇩",
            "unicode": "U+1F1F2 U+1F1E9",
            "name": "Moldova",
            "title": "flag for Moldova"
        },
        "ME": {
            "emoji": "🇲🇪",
            "unicode": "U+1F1F2 U+1F1EA",
            "name": "Montenegro",
            "title": "flag for Montenegro"
        },
        "MF": {
            "emoji": "🇲🇫",
            "unicode": "U+1F1F2 U+1F1EB",
            "name": "Saint Martin (French Part)",
            "title": "flag for Saint Martin (French Part)"
        },
        "MG": {
            "emoji": "🇲🇬",
            "unicode": "U+1F1F2 U+1F1EC",
            "name": "Madagascar",
            "title": "flag for Madagascar"
        },
        "MH": {
            "emoji": "🇲🇭",
            "unicode": "U+1F1F2 U+1F1ED",
            "name": "Marshall Islands",
            "title": "flag for Marshall Islands"
        },
        "MK": {
            "emoji": "🇲🇰",
            "unicode": "U+1F1F2 U+1F1F0",
            "name": "Macedonia",
            "title": "flag for Macedonia"
        },
        "ML": {
            "emoji": "🇲🇱",
            "unicode": "U+1F1F2 U+1F1F1",
            "name": "Mali",
            "title": "flag for Mali"
        },
        "MM": {
            "emoji": "🇲🇲",
            "unicode": "U+1F1F2 U+1F1F2",
            "name": "Myanmar",
            "title": "flag for Myanmar"
        },
        "MN": {
            "emoji": "🇲🇳",
            "unicode": "U+1F1F2 U+1F1F3",
            "name": "Mongolia",
            "title": "flag for Mongolia"
        },
        "MO": {
            "emoji": "🇲🇴",
            "unicode": "U+1F1F2 U+1F1F4",
            "name": "Macao",
            "title": "flag for Macao"
        },
        "MP": {
            "emoji": "🇲🇵",
            "unicode": "U+1F1F2 U+1F1F5",
            "name": "Northern Mariana Islands",
            "title": "flag for Northern Mariana Islands"
        },
        "MQ": {
            "emoji": "🇲🇶",
            "unicode": "U+1F1F2 U+1F1F6",
            "name": "Martinique",
            "title": "flag for Martinique"
        },
        "MR": {
            "emoji": "🇲🇷",
            "unicode": "U+1F1F2 U+1F1F7",
            "name": "Mauritania",
            "title": "flag for Mauritania"
        },
        "MS": {
            "emoji": "🇲🇸",
            "unicode": "U+1F1F2 U+1F1F8",
            "name": "Montserrat",
            "title": "flag for Montserrat"
        },
        "MT": {
            "emoji": "🇲🇹",
            "unicode": "U+1F1F2 U+1F1F9",
            "name": "Malta",
            "title": "flag for Malta"
        },
        "MU": {
            "emoji": "🇲🇺",
            "unicode": "U+1F1F2 U+1F1FA",
            "name": "Mauritius",
            "title": "flag for Mauritius"
        },
        "MV": {
            "emoji": "🇲🇻",
            "unicode": "U+1F1F2 U+1F1FB",
            "name": "Maldives",
            "title": "flag for Maldives"
        },
        "MW": {
            "emoji": "🇲🇼",
            "unicode": "U+1F1F2 U+1F1FC",
            "name": "Malawi",
            "title": "flag for Malawi"
        },
        "MX": {
            "emoji": "🇲🇽",
            "unicode": "U+1F1F2 U+1F1FD",
            "name": "Mexico",
            "title": "flag for Mexico"
        },
        "MY": {
            "emoji": "🇲🇾",
            "unicode": "U+1F1F2 U+1F1FE",
            "name": "Malaysia",
            "title": "flag for Malaysia"
        },
        "MZ": {
            "emoji": "🇲🇿",
            "unicode": "U+1F1F2 U+1F1FF",
            "name": "Mozambique",
            "title": "flag for Mozambique"
        },
        "NA": {
            "emoji": "🇳🇦",
            "unicode": "U+1F1F3 U+1F1E6",
            "name": "Namibia",
            "title": "flag for Namibia"
        },
        "NC": {
            "emoji": "🇳🇨",
            "unicode": "U+1F1F3 U+1F1E8",
            "name": "New Caledonia",
            "title": "flag for New Caledonia"
        },
        "NE": {
            "emoji": "🇳🇪",
            "unicode": "U+1F1F3 U+1F1EA",
            "name": "Niger",
            "title": "flag for Niger"
        },
        "NF": {
            "emoji": "🇳🇫",
            "unicode": "U+1F1F3 U+1F1EB",
            "name": "Norfolk Island",
            "title": "flag for Norfolk Island"
        },
        "NG": {
            "emoji": "🇳🇬",
            "unicode": "U+1F1F3 U+1F1EC",
            "name": "Nigeria",
            "title": "flag for Nigeria"
        },
        "NI": {
            "emoji": "🇳🇮",
            "unicode": "U+1F1F3 U+1F1EE",
            "name": "Nicaragua",
            "title": "flag for Nicaragua"
        },
        "NL": {
            "emoji": "🇳🇱",
            "unicode": "U+1F1F3 U+1F1F1",
            "name": "Netherlands",
            "title": "flag for Netherlands"
        },
        "NO": {
            "emoji": "🇳🇴",
            "unicode": "U+1F1F3 U+1F1F4",
            "name": "Norway",
            "title": "flag for Norway"
        },
        "NP": {
            "emoji": "🇳🇵",
            "unicode": "U+1F1F3 U+1F1F5",
            "name": "Nepal",
            "title": "flag for Nepal"
        },
        "NR": {
            "emoji": "🇳🇷",
            "unicode": "U+1F1F3 U+1F1F7",
            "name": "Nauru",
            "title": "flag for Nauru"
        },
        "NU": {
            "emoji": "🇳🇺",
            "unicode": "U+1F1F3 U+1F1FA",
            "name": "Niue",
            "title": "flag for Niue"
        },
        "NZ": {
            "emoji": "🇳🇿",
            "unicode": "U+1F1F3 U+1F1FF",
            "name": "New Zealand",
            "title": "flag for New Zealand"
        },
        "OM": {
            "emoji": "🇴🇲",
            "unicode": "U+1F1F4 U+1F1F2",
            "name": "Oman",
            "title": "flag for Oman"
        },
        "PA": {
            "emoji": "🇵🇦",
            "unicode": "U+1F1F5 U+1F1E6",
            "name": "Panama",
            "title": "flag for Panama"
        },
        "PE": {
            "emoji": "🇵🇪",
            "unicode": "U+1F1F5 U+1F1EA",
            "name": "Peru",
            "title": "flag for Peru"
        },
        "PF": {
            "emoji": "🇵🇫",
            "unicode": "U+1F1F5 U+1F1EB",
            "name": "French Polynesia",
            "title": "flag for French Polynesia"
        },
        "PG": {
            "emoji": "🇵🇬",
            "unicode": "U+1F1F5 U+1F1EC",
            "name": "Papua New Guinea",
            "title": "flag for Papua New Guinea"
        },
        "PH": {
            "emoji": "🇵🇭",
            "unicode": "U+1F1F5 U+1F1ED",
            "name": "Philippines",
            "title": "flag for Philippines"
        },
        "PK": {
            "emoji": "🇵🇰",
            "unicode": "U+1F1F5 U+1F1F0",
            "name": "Pakistan",
            "title": "flag for Pakistan"
        },
        "PL": {
            "emoji": "🇵🇱",
            "unicode": "U+1F1F5 U+1F1F1",
            "name": "Poland",
            "title": "flag for Poland"
        },
        "PM": {
            "emoji": "🇵🇲",
            "unicode": "U+1F1F5 U+1F1F2",
            "name": "Saint Pierre and Miquelon",
            "title": "flag for Saint Pierre and Miquelon"
        },
        "PN": {
            "emoji": "🇵🇳",
            "unicode": "U+1F1F5 U+1F1F3",
            "name": "Pitcairn",
            "title": "flag for Pitcairn"
        },
        "PR": {
            "emoji": "🇵🇷",
            "unicode": "U+1F1F5 U+1F1F7",
            "name": "Puerto Rico",
            "title": "flag for Puerto Rico"
        },
        "PS": {
            "emoji": "🇵🇸",
            "unicode": "U+1F1F5 U+1F1F8",
            "name": "Palestinian Territory",
            "title": "flag for Palestinian Territory"
        },
        "PT": {
            "emoji": "🇵🇹",
            "unicode": "U+1F1F5 U+1F1F9",
            "name": "Portugal",
            "title": "flag for Portugal"
        },
        "PW": {
            "emoji": "🇵🇼",
            "unicode": "U+1F1F5 U+1F1FC",
            "name": "Palau",
            "title": "flag for Palau"
        },
        "PY": {
            "emoji": "🇵🇾",
            "unicode": "U+1F1F5 U+1F1FE",
            "name": "Paraguay",
            "title": "flag for Paraguay"
        },
        "QA": {
            "emoji": "🇶🇦",
            "unicode": "U+1F1F6 U+1F1E6",
            "name": "Qatar",
            "title": "flag for Qatar"
        },
        "RE": {
            "emoji": "🇷🇪",
            "unicode": "U+1F1F7 U+1F1EA",
            "name": "Réunion",
            "title": "flag for Réunion"
        },
        "RO": {
            "emoji": "🇷🇴",
            "unicode": "U+1F1F7 U+1F1F4",
            "name": "Romania",
            "title": "flag for Romania"
        },
        "RS": {
            "emoji": "🇷🇸",
            "unicode": "U+1F1F7 U+1F1F8",
            "name": "Serbia",
            "title": "flag for Serbia"
        },
        "RU": {
            "emoji": "🇷🇺",
            "unicode": "U+1F1F7 U+1F1FA",
            "name": "Russia",
            "title": "flag for Russia"
        },
        "RW": {
            "emoji": "🇷🇼",
            "unicode": "U+1F1F7 U+1F1FC",
            "name": "Rwanda",
            "title": "flag for Rwanda"
        },
        "SA": {
            "emoji": "🇸🇦",
            "unicode": "U+1F1F8 U+1F1E6",
            "name": "Saudi Arabia",
            "title": "flag for Saudi Arabia"
        },
        "SB": {
            "emoji": "🇸🇧",
            "unicode": "U+1F1F8 U+1F1E7",
            "name": "Solomon Islands",
            "title": "flag for Solomon Islands"
        },
        "SC": {
            "emoji": "🇸🇨",
            "unicode": "U+1F1F8 U+1F1E8",
            "name": "Seychelles",
            "title": "flag for Seychelles"
        },
        "SD": {
            "emoji": "🇸🇩",
            "unicode": "U+1F1F8 U+1F1E9",
            "name": "Sudan",
            "title": "flag for Sudan"
        },
        "SE": {
            "emoji": "🇸🇪",
            "unicode": "U+1F1F8 U+1F1EA",
            "name": "Sweden",
            "title": "flag for Sweden"
        },
        "SG": {
            "emoji": "🇸🇬",
            "unicode": "U+1F1F8 U+1F1EC",
            "name": "Singapore",
            "title": "flag for Singapore"
        },
        "SH": {
            "emoji": "🇸🇭",
            "unicode": "U+1F1F8 U+1F1ED",
            "name": "Saint Helena, Ascension and Tristan Da Cunha",
            "title": "flag for Saint Helena, Ascension and Tristan Da Cunha"
        },
        "SI": {
            "emoji": "🇸🇮",
            "unicode": "U+1F1F8 U+1F1EE",
            "name": "Slovenia",
            "title": "flag for Slovenia"
        },
        "SJ": {
            "emoji": "🇸🇯",
            "unicode": "U+1F1F8 U+1F1EF",
            "name": "Svalbard and Jan Mayen",
            "title": "flag for Svalbard and Jan Mayen"
        },
        "SK": {
            "emoji": "🇸🇰",
            "unicode": "U+1F1F8 U+1F1F0",
            "name": "Slovakia",
            "title": "flag for Slovakia"
        },
        "SL": {
            "emoji": "🇸🇱",
            "unicode": "U+1F1F8 U+1F1F1",
            "name": "Sierra Leone",
            "title": "flag for Sierra Leone"
        },
        "SM": {
            "emoji": "🇸🇲",
            "unicode": "U+1F1F8 U+1F1F2",
            "name": "San Marino",
            "title": "flag for San Marino"
        },
        "SN": {
            "emoji": "🇸🇳",
            "unicode": "U+1F1F8 U+1F1F3",
            "name": "Senegal",
            "title": "flag for Senegal"
        },
        "SO": {
            "emoji": "🇸🇴",
            "unicode": "U+1F1F8 U+1F1F4",
            "name": "Somalia",
            "title": "flag for Somalia"
        },
        "SR": {
            "emoji": "🇸🇷",
            "unicode": "U+1F1F8 U+1F1F7",
            "name": "Suriname",
            "title": "flag for Suriname"
        },
        "SS": {
            "emoji": "🇸🇸",
            "unicode": "U+1F1F8 U+1F1F8",
            "name": "South Sudan",
            "title": "flag for South Sudan"
        },
        "ST": {
            "emoji": "🇸🇹",
            "unicode": "U+1F1F8 U+1F1F9",
            "name": "Sao Tome and Principe",
            "title": "flag for Sao Tome and Principe"
        },
        "SV": {
            "emoji": "🇸🇻",
            "unicode": "U+1F1F8 U+1F1FB",
            "name": "El Salvador",
            "title": "flag for El Salvador"
        },
        "SX": {
            "emoji": "🇸🇽",
            "unicode": "U+1F1F8 U+1F1FD",
            "name": "Sint Maarten (Dutch Part)",
            "title": "flag for Sint Maarten (Dutch Part)"
        },
        "SY": {
            "emoji": "🇸🇾",
            "unicode": "U+1F1F8 U+1F1FE",
            "name": "Syrian Arab Republic",
            "title": "flag for Syrian Arab Republic"
        },
        "SZ": {
            "emoji": "🇸🇿",
            "unicode": "U+1F1F8 U+1F1FF",
            "name": "Swaziland",
            "title": "flag for Swaziland"
        },
        "TC": {
            "emoji": "🇹🇨",
            "unicode": "U+1F1F9 U+1F1E8",
            "name": "Turks and Caicos Islands",
            "title": "flag for Turks and Caicos Islands"
        },
        "TD": {
            "emoji": "🇹🇩",
            "unicode": "U+1F1F9 U+1F1E9",
            "name": "Chad",
            "title": "flag for Chad"
        },
        "TF": {
            "emoji": "🇹🇫",
            "unicode": "U+1F1F9 U+1F1EB",
            "name": "French Southern Territories",
            "title": "flag for French Southern Territories"
        },
        "TG": {
            "emoji": "🇹🇬",
            "unicode": "U+1F1F9 U+1F1EC",
            "name": "Togo",
            "title": "flag for Togo"
        },
        "TH": {
            "emoji": "🇹🇭",
            "unicode": "U+1F1F9 U+1F1ED",
            "name": "Thailand",
            "title": "flag for Thailand"
        },
        "TJ": {
            "emoji": "🇹🇯",
            "unicode": "U+1F1F9 U+1F1EF",
            "name": "Tajikistan",
            "title": "flag for Tajikistan"
        },
        "TK": {
            "emoji": "🇹🇰",
            "unicode": "U+1F1F9 U+1F1F0",
            "name": "Tokelau",
            "title": "flag for Tokelau"
        },
        "TL": {
            "emoji": "🇹🇱",
            "unicode": "U+1F1F9 U+1F1F1",
            "name": "Timor-Leste",
            "title": "flag for Timor-Leste"
        },
        "TM": {
            "emoji": "🇹🇲",
            "unicode": "U+1F1F9 U+1F1F2",
            "name": "Turkmenistan",
            "title": "flag for Turkmenistan"
        },
        "TN": {
            "emoji": "🇹🇳",
            "unicode": "U+1F1F9 U+1F1F3",
            "name": "Tunisia",
            "title": "flag for Tunisia"
        },
        "TO": {
            "emoji": "🇹🇴",
            "unicode": "U+1F1F9 U+1F1F4",
            "name": "Tonga",
            "title": "flag for Tonga"
        },
        "TR": {
            "emoji": "🇹🇷",
            "unicode": "U+1F1F9 U+1F1F7",
            "name": "Turkey",
            "title": "flag for Turkey"
        },
        "TT": {
            "emoji": "🇹🇹",
            "unicode": "U+1F1F9 U+1F1F9",
            "name": "Trinidad and Tobago",
            "title": "flag for Trinidad and Tobago"
        },
        "TV": {
            "emoji": "🇹🇻",
            "unicode": "U+1F1F9 U+1F1FB",
            "name": "Tuvalu",
            "title": "flag for Tuvalu"
        },
        "TW": {
            "emoji": "🇹🇼",
            "unicode": "U+1F1F9 U+1F1FC",
            "name": "Taiwan",
            "title": "flag for Taiwan"
        },
        "TZ": {
            "emoji": "🇹🇿",
            "unicode": "U+1F1F9 U+1F1FF",
            "name": "Tanzania",
            "title": "flag for Tanzania"
        },
        "UA": {
            "emoji": "🇺🇦",
            "unicode": "U+1F1FA U+1F1E6",
            "name": "Ukraine",
            "title": "flag for Ukraine"
        },
        "UG": {
            "emoji": "🇺🇬",
            "unicode": "U+1F1FA U+1F1EC",
            "name": "Uganda",
            "title": "flag for Uganda"
        },
        "UM": {
            "emoji": "🇺🇲",
            "unicode": "U+1F1FA U+1F1F2",
            "name": "United States Minor Outlying Islands",
            "title": "flag for United States Minor Outlying Islands"
        },
        "US": {
            "emoji": "🇺🇸",
            "unicode": "U+1F1FA U+1F1F8",
            "name": "United States",
            "title": "flag for United States"
        },
        "UY": {
            "emoji": "🇺🇾",
            "unicode": "U+1F1FA U+1F1FE",
            "name": "Uruguay",
            "title": "flag for Uruguay"
        },
        "UZ": {
            "emoji": "🇺🇿",
            "unicode": "U+1F1FA U+1F1FF",
            "name": "Uzbekistan",
            "title": "flag for Uzbekistan"
        },
        "VA": {
            "emoji": "🇻🇦",
            "unicode": "U+1F1FB U+1F1E6",
            "name": "Vatican City",
            "title": "flag for Vatican City"
        },
        "VC": {
            "emoji": "🇻🇨",
            "unicode": "U+1F1FB U+1F1E8",
            "name": "Saint Vincent and The Grenadines",
            "title": "flag for Saint Vincent and The Grenadines"
        },
        "VE": {
            "emoji": "🇻🇪",
            "unicode": "U+1F1FB U+1F1EA",
            "name": "Venezuela",
            "title": "flag for Venezuela"
        },
        "VG": {
            "emoji": "🇻🇬",
            "unicode": "U+1F1FB U+1F1EC",
            "name": "Virgin Islands, British",
            "title": "flag for Virgin Islands, British"
        },
        "VI": {
            "emoji": "🇻🇮",
            "unicode": "U+1F1FB U+1F1EE",
            "name": "Virgin Islands, U.S.",
            "title": "flag for Virgin Islands, U.S."
        },
        "VN": {
            "emoji": "🇻🇳",
            "unicode": "U+1F1FB U+1F1F3",
            "name": "Viet Nam",
            "title": "flag for Viet Nam"
        },
        "VU": {
            "emoji": "🇻🇺",
            "unicode": "U+1F1FB U+1F1FA",
            "name": "Vanuatu",
            "title": "flag for Vanuatu"
        },
        "WF": {
            "emoji": "🇼🇫",
            "unicode": "U+1F1FC U+1F1EB",
            "name": "Wallis and Futuna",
            "title": "flag for Wallis and Futuna"
        },
        "WS": {
            "emoji": "🇼🇸",
            "unicode": "U+1F1FC U+1F1F8",
            "name": "Samoa",
            "title": "flag for Samoa"
        },
        "YE": {
            "emoji": "🇾🇪",
            "unicode": "U+1F1FE U+1F1EA",
            "name": "Yemen",
            "title": "flag for Yemen"
        },
        "YT": {
            "emoji": "🇾🇹",
            "unicode": "U+1F1FE U+1F1F9",
            "name": "Mayotte",
            "title": "flag for Mayotte"
        },
        "ZA": {
            "emoji": "🇿🇦",
            "unicode": "U+1F1FF U+1F1E6",
            "name": "South Africa",
            "title": "flag for South Africa"
        },
        "ZM": {
            "emoji": "🇿🇲",
            "unicode": "U+1F1FF U+1F1F2",
            "name": "Zambia",
            "title": "flag for Zambia"
        },
        "ZW": {
            "emoji": "🇿🇼",
            "unicode": "U+1F1FF U+1F1FC",
            "name": "Zimbabwe",
            "title": "flag for Zimbabwe"
        }
    }
