#Replacing the namespace/username/password in the secret-template file with env variable 
#!/bin/sh
export NAMESPACE=production
export DB_USERNAME=prod-admin
export DB_PASSWORD=Dhhs22kfid9c
sed -e 's/%NAMESPACE%/staging/' \
    -e 's/%DB_USERNAME%/admin/'          \
    -e 's/%DB_PASSWORD%/secret/'     \
    ./secret-template.yaml


file_path="./secret-template.yaml"
env_var_names=$(env | sed -E -n 's/^([^=]+)(=.*)/\1/p')

for env_var_name in ${env_var_names}; do
    echo "Checking for '${env_var_name}'..."

    if grep -q "%${env_var_name}%" "${file_path}"; then
        echo "-> Found '${env_var_name}', expanding now..."

        env_var_value="${!env_var_name}"
        escaped_env_var_value=$(echo ${env_var_value} | sed -e 's/[\/&]/\\&/g')

        sed -e "s/%${env_var_name}%/${escaped_env_var_value}/" \
            "${file_path}" > "${file_path}.tmp"
        mv "${file_path}.tmp" "${file_path}"
    fi
done

