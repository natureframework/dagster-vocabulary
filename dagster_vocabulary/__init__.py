from dagster import Definitions
from .assets.definitions import definitions
from .assets.partitions import partitions
from .assets.piece import piece
from .assets.words import words

defs = Definitions(assets=[piece, words, partitions, definitions])
