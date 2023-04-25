import requests

url = 'https://reqres.in/api/users'
site = requests.get(url)
class TestApi():
    def test_1(self):
        actual = site
        assert 200 <= actual.status_code < 400
    def test_2(self):
        dict1 = site.json()
        actual = dict1['data'][2]['email']
        expected = 'emma.wong@reqres.in'
        assert actual == expected
