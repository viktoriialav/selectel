from typing import Optional, Annotated, Literal

from pydantic import BaseModel, StringConstraints


class PricePlan(BaseModel):
    commitment_period: Optional[int]
    dead: int
    discount: Optional[int]
    grace: int
    name: Optional[str]
    not_available_for_a_reason: Optional[
        Literal['free', 'non_resident', 'reseller_owner_mismatch', 'unavailable', None]]
    period: Optional[int]
    type: Optional[Literal['free', 'hour', 'day', 'month', 'year', 'service']]
    uuid: Optional[Annotated[str, StringConstraints(min_length=36, max_length=36)]]


class ListPricePlans(BaseModel):
    execution_time: Optional[float]
    item_count: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    progress: Optional[int]
    result: PricePlan | list[PricePlan]
    status: Optional[str]
    task_id: Annotated[str, StringConstraints(min_length=36, max_length=36)]
