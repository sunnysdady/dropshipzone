import asyncio
from api.orders import OrderAPI

class OrderService:
    def __init__(self):
        self.api = OrderAPI()

    async def list_orders(self, **filters):
        return await self.api.list(**filters)

    async def cancel_orders(self, orders):
        return await self.api.cancel(orders)
