from x4_mcp.server import MCPServer


def test_health():
    s = MCPServer()
    h = s.health()
    assert h["status"] == "ok"
    assert h["server"] == "x4-mcp"


def test_register_and_list():
    s = MCPServer()
    s.register_tool("ping", lambda: "pong")
    assert s.list_tools() == ["ping"]
