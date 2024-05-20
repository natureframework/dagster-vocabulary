from typing import Set
from dagster import AssetExecutionContext, asset
from dagster_pieces.partitions.reset import reset


@asset(key_prefix="vocabulary")
def partitions(context: AssetExecutionContext, words: Set[str]) -> None:
    reset(context.instance, "words", list(words))
