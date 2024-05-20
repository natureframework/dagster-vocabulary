from dagster import AssetKey, SourceAsset
from dagster_vocabulary.defs.partitions.references import references

pieces = SourceAsset(AssetKey("pieces"), partitions_def=references)
