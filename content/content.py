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

data = r.json()
#print(data)
#print(data['score'])

# statut de la requête
status_code = r.status_code

sentence=sys.argv[3]

if (data['score'] > 0) and (sentence =="life is beautiful"):
    statut_score = True
elif (data['score'] < 0) and (sentence =="that sucks"):
    statut_score = True
else:
    statut_score = False

# affichage des résultats
if (status_code == 200) and (statut_score == True) :
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'



output = '''
============================
    Content test
============================

request done at "{version}/sentiment"
| username={user}
| password={pwd}
| sentence={sentence}
| score={score}
| statut_score={statut_score}



expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

print(output.format(status_code=status_code, test_status=test_status, user=sys.argv[1], pwd=sys.argv[2], sentence=sys.argv[3], version=sys.argv[4], score=data['score'], statut_score=statut_score))

# impression dans un fichier
log_enabled = int(os.getenv('LOG'))
if log_enabled == 1:
    print('- LOG is enabled !')
    with open('/app/data/api_test.log', 'a') as file:
        file.write(output)