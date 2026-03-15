from pydantic import BaseModel , Field ,HttpUrl , ValidationError
from ..logs.loger import logger




class Rating(BaseModel):
    rate: float = Field(ge=0,le=5)
    count: int = Field(ge=0)


class OrderRecord(BaseModel):
    id: int
    title: str
    price:float = Field(ge=0)
    description: str
    category: str
    image: HttpUrl
    rating: Rating
    


def validate_order(raw: dict) -> OrderRecord | None:
    try:
        record: OrderRecord = OrderRecord(**raw)
        logger.info("Валідація Успішна")
        return record
    except ValidationError:
        return None