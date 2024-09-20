from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints


class ResourceModel(BaseModel):
    pass


class ListResources(BaseModel):
    execution_time: Optional[float]
    item_count: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    progress: Optional[int]
    result: list[ResourceModel]
    status: Optional[str]
    task_id: Annotated[str, StringConstraints(min_length=36, max_length=36)]


class BillingStatsModel(BaseModel):
    unpaid_sum: float


class ResourceBillingInfo(BaseModel):
    execution_time: Optional[float]
    item_count: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    progress: Optional[int]
    result: BillingStatsModel
    status: Optional[str]
    task_id: Annotated[str, StringConstraints(min_length=36, max_length=36)]
