from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints


class ResourceTagModel(BaseModel):
    uuid: Annotated[str, StringConstraints(min_length=36, max_length=36)]
    name: Annotated[str, StringConstraints(max_length=64)]


class CreatedResourceTag(BaseModel):
    execution_time: Optional[float]
    item_count: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    progress: Optional[int]
    result: ResourceTagModel
    status: Optional[str]
    task_id: Annotated[str, StringConstraints(min_length=36, max_length=36)]


class UpdatedResourceTag(CreatedResourceTag):
    pass


class DeletedResourceTag(CreatedResourceTag):
    pass


class ListResourceTags(BaseModel):
    execution_time: Optional[float]
    item_count: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    progress: Optional[int]
    result: ResourceTagModel | list[ResourceTagModel]
    status: Optional[str]
    task_id: Annotated[str, StringConstraints(min_length=36, max_length=36)]


class ResourceTagRequestBody(BaseModel):
    name: Annotated[str, StringConstraints(max_length=64)]
