import logging
import json

# Inicialização global de logging estruturado para tools
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record)

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logging.basicConfig(level=logging.INFO, handlers=[handler])
import os

from crewai_tools.adapters.zapier_adapter import ZapierActionTool, ZapierActionsAdapter


logger = logging.getLogger(__name__)


def ZapierActionTools(  # noqa: N802
    zapier_api_key: str | None = None, action_list: list[str] | None = None
) -> list[ZapierActionTool]:
    """Factory function that returns Zapier action tools.

    Args:
        zapier_api_key: The API key for Zapier.
        action_list: Optional list of specific tool names to include.

    Returns:
        A list of Zapier action tools.
    """
    if zapier_api_key is None:
        zapier_api_key = os.getenv("ZAPIER_API_KEY")
        if zapier_api_key is None:
            logger.error("ZAPIER_API_KEY is not set")
            raise ValueError("ZAPIER_API_KEY is not set")
    adapter = ZapierActionsAdapter(zapier_api_key)
    all_tools = adapter.tools()

    if action_list is None:
        return all_tools

    return [tool for tool in all_tools if tool.name in action_list]
