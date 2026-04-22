import os
import httpx
from .auth import AuthClient
from utils.logger import logger
from typing import Dict, Any

class BaseClient:
    def __init__(self):
        self.auth = AuthClient()
        self.base_url = os.getenv("DSZ_BASE_URL")
        self.client = httpx.AsyncClient(timeout=30)

    async def request(self, method: str, path: str,
                      *, json: Dict = None, params: Dict = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        headers = {"Authorization": f"jwt {await self.auth.get_token()}"}
        try:
            resp = await self.client.request(method, url,
                                             headers=headers,
                                             json=json,
                                             params=params)
            resp.raise_for_status()
            return {"success": True, "data": resp.json()}
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 401:
                # token 失效，重新获取后再尝试一次
                logger.warning("Token expired – refreshing")
                await self.auth.get_token()
                return await self.request(method, path, json=json, params=params)
            logger.error(f"API error {exc.response.status_code}: {exc.response.text}")
            return {"success": False, "error": exc.response.text}
        except httpx.RequestError as exc:
            logger.error(f"Network error: {exc}")
            return {"success": False, "error": str(exc)}
