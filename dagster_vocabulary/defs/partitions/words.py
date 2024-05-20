from dagster import DynamicPartitionsDefinition

words = DynamicPartitionsDefinition(name="words")
