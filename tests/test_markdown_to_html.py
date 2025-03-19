from markdown_to_html import html_to_md


def test_binding() -> None:
    result = html_to_md("<h1>Test</h1>")
    assert result.strip() == "# Test"
