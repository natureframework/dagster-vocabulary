from urllib.parse import quote
from .group.get import get as get_group


def get(word: str) -> str:
    group = quote(get_group(word))
    word = quote(word)
    return (
        "https://raw.githubusercontent.com"
        "/ivandustin"
        "/dictionary"
        "/main"
        "/data"
        "/new"
        f"/{group}"
        f"/{word}.txt"
    )
