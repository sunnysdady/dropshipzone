from .base_client import BaseClient

class ShipmentAPI:
    def __init__(self):
        self.client = BaseClient()

    async def list(self, order_ids: str):
        return await self.client.request("GET", "/shipments", params={"order_ids": order_ids})

    async def create(self, shipments):
        return await self.client.request("POST", "/shipments", json={"shipments": shipments})

    async def delete(self, order_id: str, tracking_number: str):
        return await self.client.request(
            "DELETE",
            "/shipments",
            params={"order_id": order_id, "tracking_number": tracking_number},
        )
