from typing import Annotated, Optional, Union

from pydantic import BaseModel, StringConstraints, Field


class PricePeriodModel(BaseModel):
    day: Union[float, None]
    hour: Union[float, None]
    month: Union[float, None]
    year: Union[float, None]


class PriceModel(BaseModel):
    EUR: PricePeriodModel
    KES: PricePeriodModel
    KZT: PricePeriodModel
    RUB: PricePeriodModel
    USD: PricePeriodModel
    UZS: PricePeriodModel


class ServicePlanAvailable(BaseModel):
    count: int
    plan_uuid: Annotated[str, StringConstraints(min_length=36, max_length=36)]


class ServiceAvailable(BaseModel):
    count: int
    location: Annotated[str, StringConstraints(min_length=36, max_length=36)]
    plan_count: list[ServicePlanAvailable]


class ServiceTag(BaseModel):
    is_filter: bool
    is_hide: bool
    name: str
    sort_weight: int
    style_key: str
    text: str
    uuid: Annotated[str, StringConstraints(min_length=36, max_length=36)]


class ServiceBase(BaseModel):
    available: list[ServiceAvailable]
    eol_date: Optional[int]
    is_order: bool
    is_preorder: bool
    is_price_plan_discount_enabled: bool
    is_primary: bool
    is_qchange: bool
    is_single_prolonged: bool
    is_user_discount_enabled: bool
    location_price_collection: Union[dict[str, PriceModel], None]
    model: str
    name: str
    price_collection: PriceModel
    quantity: Optional[int]
    service_tag: str
    setup_fee_collection: PriceModel
    state: str
    tag_list: list[ServiceTag]
    tags: Union[list[str], None]
    tariff_line: Union[str, None]
    uuid: Annotated[str, StringConstraints(min_length=36, max_length=36)]


class ListServices(BaseModel):
    execution_time: Optional[float]
    item_count: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    progress: Optional[int]
    result: list[ServiceBase]
    status: Optional[str]
    task_id: Annotated[str, StringConstraints(min_length=36, max_length=36)]


class ServiceColocationUuidBillingRequestBody(BaseModel):
    campaign_uuid: Optional[str] = None
    location_uuid: Annotated[str, StringConstraints(min_length=36, max_length=36)]
    pay_day: Optional[Annotated[int, Field(ge=1, default=1)]] = None
    price_plan_uuid: Annotated[str, StringConstraints(min_length=36, max_length=36)]
    quantity: Optional[Annotated[int, Field(ge=1, default=1)]]


class DiscountFromCampaigns(BaseModel):
    pass


class DiscountDetailModel(BaseModel):
    discounts_from_campaigns: DiscountFromCampaigns
    price_plan: int
    resource: int
    user: int


class NextPriceModel(BaseModel):
    amount_due: float
    debt: float
    discount: int
    discount_detail: DiscountDetailModel
    due_date: Optional[int]
    future_price: float
    paid_till: Optional[int]
    plan_price: float
    setup_fee: int


class PricePlanModel(BaseModel):
    name: str
    period: int
    type: str
    uuid: Annotated[str, StringConstraints(min_length=36, max_length=36)]


class BillingModel(BaseModel):
    currency: str
    current_price_plan: PricePlanModel
    next_price_plan: PricePlanModel
    price: Optional[NextPriceModel]


class ServiceColocationUuidBillingModel(BaseModel):
    execution_time: Optional[float]
    item_count: Optional[int]
    limit: Optional[int]
    page: Optional[int]
    progress: Optional[int]
    result: BillingModel
    status: Optional[str]
    task_id: Annotated[str, StringConstraints(min_length=36, max_length=36)]
