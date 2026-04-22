import asyncio
from api.shipments import ShipmentAPI

class ShipmentService:
    def __init__(self):
        self.api = ShipmentAPI()

    async def list_shipments(self, order_ids: str):
        return await self.api.list(order_ids)

    async def create_shipments(self, shipments):
        return await self.api.create(shipments)

    async def delete_shipment(self, order_id: str, tracking_number: str):
        return await self.api.delete(order_id, tracking_number)
