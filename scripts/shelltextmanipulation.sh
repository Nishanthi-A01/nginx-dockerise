#Replacing the namespace/username/password in the secret-template file with env variable 
#!/bin/sh
sed -e 's/%NAMESPACE%/staging/' \
    -e 's/%DB_USERNAME%/admin/'          \
    -e 's/%DB_PASSWORD%/secret/'     \
    ./secret-template.yaml


