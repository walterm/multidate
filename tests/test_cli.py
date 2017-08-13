import mock
import pytest

from multidate import cli


@pytest.mark.parametrize('input_str,expected', [
    ('1502586219', [1502586219]),
    ('1502586219,1502586220', [1502586219, 1502586220]),
    ('test', None)
])
def test_sanatize_hour(input_str, expected):
    if expected is not None:
        assert cli.sanatize_hour(input_str) == expected
    else:
        with mock.patch('multidate.cli.handle_exit') as exit_call:
            cli.sanatize_hour(input_str)
            exit_call.assert_called_once()
