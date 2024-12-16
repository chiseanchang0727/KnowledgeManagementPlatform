from enum import Enum

class InputFileType(str, Enum):

    csv = "csv"
    txt = "txt"
    pdf = "pdf"

    def __repr__(self):
        return f'"{self.value}"'