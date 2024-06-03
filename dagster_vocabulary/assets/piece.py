from dagster import AssetKey, SourceAsset
from dagster_vocabulary.defs.partitions.references import references

piece = SourceAsset(AssetKey("piece"), partitions_def=references)
