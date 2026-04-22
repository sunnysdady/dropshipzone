from .base_client import BaseClient

class OrderAPI:
    def __init__(self):
        self.client = BaseClient()

    async def list(self, **params):
        return await self.client.request("GET", "/orders", params=params)

    async def cancel(self, orders):
        return await self.client.request("PUT", "/orders/cancel", json={"orders": orders})
