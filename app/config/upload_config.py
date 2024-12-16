from pydantic import BaseModel, Field
from typing import Optional



class UploadConfig(BaseModel):

    dir: str = Field(
        default=None,
        description="the path for saving user upload files."
    )