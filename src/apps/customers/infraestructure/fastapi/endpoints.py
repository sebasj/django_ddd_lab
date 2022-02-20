from fastapi import APIRouter, Depends, HTTPException

from apps.customers.application import customers_use_cases 

from apps.customers.infraestructure.fastapi.serializers import CustomerSerializer
from apps.customers.infraestructure.fastapi.repositories import CustomerFastAPIRepository

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def customers_list_api_view():
    use_case = customers_use_cases.CustomersListUseCase(customers_repository=CustomerFastAPIRepository())
    customers = use_case.execute()
    return customers


@router.post("/add")
async def customers_list_api_view(customer: CustomerSerializer):
    use_case = customers_use_cases.CustomerCreateUseCase(customers_repository=CustomerFastAPIRepository())
    customers = use_case.create(customer.name, customer.phone_number, customer.email, customer.vat_id)
    return customers

