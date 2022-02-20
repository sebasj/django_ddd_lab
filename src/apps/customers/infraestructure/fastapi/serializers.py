from pydantic import BaseModel, Field


class CustomerSerializer(BaseModel):
    name: str
    phone_number: str
    email: str
    vat_id: str
