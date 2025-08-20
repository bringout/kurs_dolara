import pytest
from unittest.mock import patch
from kurs_dolara.main import get_usd_rate

@patch('requests.get')
def test_get_usd_rate(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = '''
    <tr>
        <td>USD</td>
        <td>840</td>
        <td class="tbl-smaller tbl-highlight tbl-center middle-column">1.674225</td>
    </tr>
    <tr>
        <td>XDR</td>
        <td>960</td>
        <td class="tbl-smaller tbl-highlight tbl-center middle-column">2.293074</td>
    </tr>
    '''
    rate = get_usd_rate()
    assert rate == "1.674225"