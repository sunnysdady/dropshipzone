import asyncio
from api.products import ProductAPI

class ProductService:
    def __init__(self):
        self.api = ProductAPI()

    async def list_all(self, **filters):
        return await self.api.list(**filters)

    async def batch_add(self, products, batch=200):
        tasks = []
        for i in range(0, len(products), batch):
            batch_data = products[i:i+batch]
            tasks.append(self.api.add(batch_data))
        return await asyncio.gather(*tasks)

    async def batch_update_stock(self, sku_stock_list, batch=500):
        tasks = []
        for i in range(0, len(sku_stock_list), batch):
            batch_data = {"products": sku_stock_list[i:i+batch]}
            tasks.append(self.api.update_stock(batch_data["products"]))
        return await asyncio.gather(*tasks)

    async def batch_update_status(self, sku_status_list, batch=500):
        tasks = []
        for i in range(0, len(sku_status_list), batch):
            batch_data = {"products": sku_status_list[i:i+batch]}
            tasks.append(self.api.update_status(batch_data["products"]))
        return await asyncio.gather(*tasks)

    async def batch_update_content(self, product_content_list, batch=200):
        tasks = []
        for i in range(0, len(product_content_list), batch):
            batch_data = {"products": product_content_list[i:i+batch]}
            tasks.append(self.api.update_content(batch_data["products"]))
        return await asyncio.gather(*tasks)
