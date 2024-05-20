from dagster import AssetExecutionContext, asset
from dagster_vocabulary.defs.partitions.words import words
from dagster_vocabulary.url.read import read
from dagster_vocabulary.url.get import get


@asset(partitions_def=words)
def definitions(context: AssetExecutionContext) -> str:
    return read(get(context.partition_key))
