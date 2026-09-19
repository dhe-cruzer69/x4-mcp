"""Minimal MCP server scaffold.

This module deliberately provides only structural placeholders.
No production behavior is claimed until evidence states advance past L0.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class MCPServer:
    """Registry-aware MCP server skeleton."""

    name: str = "x4-mcp"
    version: str = "0.0.1"
    tools: dict[str, Any] = field(default_factory=dict)

    def register_tool(self, name: str, handler: Any) -> None:
        if not name or not callable(handler):
            raise ValueError("tool name and callable handler are required")
        self.tools[name] = handler

    def list_tools(self) -> list[str]:
        return sorted(self.tools)

    def health(self) -> dict[str, str]:
        return {"status": "ok", "server": self.name, "version": self.version}
