from dagster import Definitions
from .assets.pieces import pieces
from .assets.words import words

defs = Definitions(assets=[pieces, words])
