import os
import json
import time
import httpx
from utils.logger import logger
from pathlib import Path

CACHE_PATH = Path(".token_cache.json")

class AuthClient:
    def __init__(self):
        self.base_url = os.getenv("DSZ_BASE_URL")
        self.email = os.getenv("DSZ_EMAIL")
        self.password = os.getenv("DSZ_PASSWORD")
        self.token = None
        self.exp = 0
        self._load_cache()

    def _load_cache(self):
        if CACHE_PATH.exists():
            data = json.loads(CACHE_PATH.read_text())
            self.token = data.get("token")
            self.exp = data.get("exp", 0)

    def _save_cache(self, token: str, exp: int):
        CACHE_PATH.write_text(json.dumps({"token": token, "exp": exp}))
        self.token, self.exp = token, exp

    def _valid(self) -> bool:
        return self.token and time.time() < self.exp - 30   # 提前 30s 刷新

    async def get_token(self) -> str:
        if self._valid():
            return self.token
        logger.info("Fetching new JWT token …")
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{self.base_url}/auth",
                json={"email": self.email, "password": self.password},
                timeout=15,
            )
        resp.raise_for_status()
        payload = resp.json()["data"]
        self._save_cache(payload["token"], payload["exp"])
        return self.token
