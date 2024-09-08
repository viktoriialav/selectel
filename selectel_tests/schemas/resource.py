from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints, Field


class ListResources(BaseModel):
    execution_time: Optional[float]
    item_count: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    progress: Optional[int]
    result: list[dict] = []
    status: Optional[str]
    task_id: Annotated[str, StringConstraints(min_length=36, max_length=36)]



