from enum import Enum

class InputFileType(str, Enum):

    csv = "csv"
    text = "text"
    pdf = "pdf"

    def __repr__(self):
        return f'"{self.value}"'