from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)

product = Product(
    name="Laptop",
    price=500000,
    quantity=2
)

print(product)