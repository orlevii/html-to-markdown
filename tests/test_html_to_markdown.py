from go_html_to_markdown import html_to_markdown


def test_binding() -> None:
    result = html_to_markdown("<h1>Test</h1>")
    assert result.strip() == "# Test"
