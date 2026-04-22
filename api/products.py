from .base_client import BaseClient

class ProductAPI:
    def __init__(self):
        self.client = BaseClient()

    async def list(self, **params):
        return await self.client.request("GET", "/products", params=params)

    async def add(self, products):
        return await self.client.request("POST", "/products", json={"products": products})

    async def update_content(self, products):
        return await self.client.request("PUT", "/products/content", json={"products": products})

    async def update_status(self, products):
        return await self.client.request("PUT", "/products/status", json={"products": products})

    async def update_stock(self, products):
        return await self.client.request("PUT", "/products/stock", json={"products": products})
