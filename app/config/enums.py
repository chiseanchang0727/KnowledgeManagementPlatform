from enum import Enum

class InputFileType(str, Enum):
    """The input file type for the pipeline."""

    csv = "csv"
    """The CSV input type."""
    text = "text"
    """The text input type."""

    def __repr__(self):
        """Get a string representation."""
        return f'"{self.value}"'