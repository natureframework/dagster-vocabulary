from typing import Dict, Set
from pandas import DataFrame, concat
from dagster import asset


@asset
def words(piece: Dict[str, DataFrame]) -> Set[str]:
    return set(concat(piece.values())["word"])
