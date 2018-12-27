import json
from unittest import mock

from mock import mock_open


def validate_config(config_file):
    with open(config_file) as cf:
        j = json.load(cf)
        return 'exp_dir' in j


def test_validate_config_for_requ_param():
    with mock.patch('builtins.open', mock_open(read_data="{\"exp_dir\":\"/tmp\"}")) as m:
        assert validate_config('config.json')
        m.assert_called_with('config.json')
