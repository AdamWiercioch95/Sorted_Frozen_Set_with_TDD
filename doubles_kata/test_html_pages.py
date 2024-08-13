import io

from doubles_kata.html_pages import HtmlPagesConverter


# fake
def test_convert_quotes():
    fake_file = io.StringIO("quote: ' ")
    html_conv = HtmlPagesConverter(open_file=fake_file)
    converted_text = html_conv.get_html_page(0)
    assert converted_text == "quote: &#x27;<br />"


def test_access_second_page():
    fake_file = io.StringIO("""page 1
 PAGE_BREAK
 page 2
 PAGE_BREAK
 page 3""")
    html_conv = HtmlPagesConverter(open_file=fake_file)
    converted_text = html_conv.get_html_page(1)
    assert converted_text == "page 2<br />"
