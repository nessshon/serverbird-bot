from dataclasses import dataclass

import aiohttp

from bs4 import BeautifulSoup
from countries import Country, CountryNotFoundError


class ParserError(Exception):
    ...


@dataclass
class ChatMessage:
    map: str
    date: str
    text: str
    user_name: str
    user_link: str
    user_country: str


async def fetch_html_page(url) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            match response.status:
                case 200:
                    return await response.text()
                case _:
                    raise ParserError(response.status, response.reason)


async def parse_chat(base_url: str) -> None | list[ChatMessage]:
    url = base_url + "/stats/hlstats.php?mode=chat&game=l4d"  # noqa

    try:
        data: list[ChatMessage] = []
        html = await fetch_html_page(url)
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", class_="data-table")

        for row in table.find_all("tr")[1:]:
            try:
                county_code = row.find("img")["src"].split("/")[-1].split(".")[0]
                country_emoji = Country.get_emoji(code=county_code.upper())
            except CountryNotFoundError:
                country_emoji = "🏴‍☠️"

            data.append(
                ChatMessage(
                    map=row.find_all("td")[4].text.strip(),
                    date=row.find_all("td")[0].text.strip(),
                    text=row.find_all("td")[2].text.strip(),
                    user_name=row.find("a").text.strip(),
                    user_link=base_url + row.find("a")["href"],
                    user_country=country_emoji,
                )
            )

        return data

    except ParserError:
        ...

    return None
