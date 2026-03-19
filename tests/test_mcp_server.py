def test_mcp_server_imports():
    from paper_search.transports import mcp_server
    assert hasattr(mcp_server, "mcp")
    assert hasattr(mcp_server, "main")
