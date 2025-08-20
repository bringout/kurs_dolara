
import pytest
from unittest.mock import patch
from pypi_hello.main import get_usd_rate

@patch('requests.get')
def test_get_usd_rate(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = '''
    <td class="tbl-smaller tbl-center">840</td>
    <td class="tbl-smaller tbl-center buysell-column" style="display:none;">1.670039</td>
    <td class="tbl-smaller tbl-highlight tbl-center middle-column">1.674225</td>
    '''
    rate = get_usd_rate()
    assert rate == "1.674225"
