from loguru import logger
import os
from pathlib import Path

log_path = os.getenv("DSZ_LOG_PATH", "logs/dsz_tool.log")
Path("logs").mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stderr, level="INFO", colorize=True)
logger.add(log_path, rotation="10 MB", retention="30 days",
           serialize=True, level="DEBUG")
