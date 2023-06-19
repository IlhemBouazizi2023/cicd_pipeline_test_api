# login à docker-hub
docker login

# création de l'image docker pour le test de l'authentification
cd authentication/
docker build -t authentication_test .
docker tag authentication_test:latest ilhemb/evaluation_docker_authentication:v19
docker push ilhemb/evaluation_docker_authentication:v19

# création de l'image docker pour le test de l'authorisation
cd authorization/
docker build -t authorization_test .
docker tag authorization_test:latest ilhemb/evaluation_docker_authorization:v19
docker push ilhemb/evaluation_docker_authorization:v19

# création de l'image docker pour le contenu
cd content/
docker build -t content_test .
docker tag content_test:latest ilhemb/evaluation_docker_content:v19
docker push ilhemb/evaluation_docker_content:v19

# lancer docker-compose.yml
docker-compose up
