import csv

from task_2 import parse_page, save_to_file


def test_parse_page():
    sample_html = """
    <html><body><div id="mw-pages"><div class="mw-category-group">
    <h3>А</h3>
    <ul>
        <li>Аист</li>
        <li>Акула</li>
    </ul>
    </div></div></body></html>
    """

    class FakeResponse:
        def __init__(self, content):
            self.content = content

    result = {}
    site_url, result = parse_page(FakeResponse(sample_html.encode()), result)

    assert site_url is None
    assert result == {'А': 2}


def test_save_to_file():
    result = {'А': 2, 'Б': 3}
    filename = 'task_2/beasts_test.csv'
    save_to_file(result, filename)
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        assert rows == [['А', '2'], ['Б', '3']]


def test_parse_page_without_categories():
    sample_html = """
    <html><body>
    </body></html>
    """

    class FakeResponse:
        def __init__(self, content):
            self.content = content

    result = {}
    site_url, result = parse_page(FakeResponse(sample_html.encode()), result)
    assert site_url is None
    assert result == {}
