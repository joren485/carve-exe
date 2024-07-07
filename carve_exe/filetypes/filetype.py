from typing import BinaryIO


class Filetype:
    """Abstract Carver."""

    NAME: str = None
    MAGIC: bytes = None

    # 100 MB
    DEFAULT_MAX_SIZE = 100000000

    @classmethod
    def get_size(cls, h_input: BinaryIO) -> int | None:
        """TEST."""
        raise NotImplementedError
