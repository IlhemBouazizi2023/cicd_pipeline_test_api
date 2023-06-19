import os
import sys
import requests

# définition de l'adresse de l'API
api_address = '99.80.68.99'
# port de l'API
api_port = 8000

# le paramètre version v1 ou v2
api_version = sys.argv[4]

# requête
r = requests.get(
    url='http://{address}:{port}/{api}/sentiment'.format(address=api_address, port=api_port, api=api_version),
    params= {
        'username': sys.argv[1],
        'password': sys.argv[2],
        'sentence': sys.argv[3]
    }
)

output = '''
============================
    Authorization test
============================

request done at "{version}/sentiment"
| username={user}
| password={pwd}
| sentence={sentence}



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
print(output.format(status_code=status_code, test_status=test_status, user=sys.argv[1], pwd=sys.argv[2], sentence=sys.argv[3], version=sys.argv[4]))

# impression dans un fichier
log_enabled = int(os.getenv('LOG'))
if log_enabled == 1:
    print('- LOG is enabled !')
    with open('/app/data/api_test.log', 'a') as file:
        file.write(output)