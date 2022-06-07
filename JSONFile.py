import requests
in_values = {'email': "editor_nhance@haltian.com", 'password': "hgbfA!!23#aE"}
res = requests.post('http://eu-api.empathicbuilding.com/v1/login', data=in_values)
print(res.text)
