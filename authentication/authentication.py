import os
import sys
import requests

# définition de l'adresse de l'API
api_address = '99.80.68.99'
# port de l'API
api_port = 8000

# requête
r = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': sys.argv[1],
        'password': sys.argv[2]
    }
)

output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username={user}
| password={pwd}

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status, user=sys.argv[1], pwd=sys.argv[2]))

# impression dans un fichier
print('- Checking if LOG is enabled')


log_enabled = int(os.getenv('LOG'))
if log_enabled == 1:
    print('- LOG is enabled !')
    with open('/app/data/api_test.log', 'a') as file:
        file.write(output)