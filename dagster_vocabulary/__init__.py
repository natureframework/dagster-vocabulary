from dagster import Definitions
from .assets.definitions import definitions
from .assets.partitions import partitions
from .assets.pieces import pieces
from .assets.words import words

defs = Definitions(assets=[pieces, words, partitions, definitions])
