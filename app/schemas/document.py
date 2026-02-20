from pydantic import BaseModel

class DocumentIngestionResponse(BaseModel):
    file_name: str
    raw_path: str
    text_path: str
    content_preview: str
