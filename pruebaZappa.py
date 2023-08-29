# Importar el SDK de AWS
import boto3

# Obtener la función de Lambda
lambda_client = boto3.client("lambda")
function_name = "my-function-name"

# Obtener la versión actual de la función
latest_version = lambda_client.get_function(FunctionName=function_name)["Version"]

# Verificar si la función tiene una versión
if latest_version is None:
    # La función no tiene una versión, por lo que se debe realizar un deploy
    zappa deploy
else:
    # La función tiene una versión, por lo que se debe realizar un update
    zappa update