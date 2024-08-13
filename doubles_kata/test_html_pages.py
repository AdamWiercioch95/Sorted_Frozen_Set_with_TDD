import io

from doubles_kata.html_pages import HtmlPagesConverter


# fake
def test_convert_quotes():
    fake_file = io.StringIO("quote: ' ")
    html_conv = HtmlPagesConverter(open_file=fake_file)
    converted_text = html_conv.get_html_page(0)
    assert converted_text == "quote: &#x27;<br />"
