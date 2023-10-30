from urllib.parse import quote # por causa do @ na senha...
from dotenv import load_dotenv, find_dotenv
import os
# localiza o arquivo de .env
dotenv_file = find_dotenv()
# Carrega o arquivo .env
load_dotenv(dotenv_file)
# Configurações da APP
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DEBUG = os.getenv("DEBUG")
# Configurações da API
URL_API = os.getenv("URL_API")
HEADERS_API = {'x-token': os.getenv("X_TOKEN"), 'x-key': os.getenv("X_KEY")}
# Configuração dos endpoints
ENDPOINT_LOGIN = os.getenv("ENDPOINT_LOGIN")
ENDPOINT_FUNCIONARIO = os.getenv("ENDPOINT_FUNCIONARIO")
ENDPOINT_CLIENTE = os.getenv("ENDPOINT_CLIENTE")
ENDPOINT_PRODUTO = os.getenv("ENDPOINT_PRODUTO")

# Configurações banco de dados
DB_SGDB = os.getenv("DB_SGDB")
DB_NAME = os.getenv("DB_NAME")
# Caso seja diferente de sqlite
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = quote(os.getenv("DB_PASS"))

# Ajusta STR_DATABASE conforme gerenciador escolhido
if DB_SGDB == 'sqlite': # SQLite
    STR_DATABASE = f"sqlite:///{DB_NAME}.db"
# elif DB_SGDB == 'mysql': # MySQL
#     import pymysql
#     STR_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
# elif DB_SGDB == 'mssql': # SQL Server
#     import pymssql
#     STR_DATABASE = f"mssql+pymssql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8"
else: # SQLite
    STR_DATABASE = f"sqlite:///apiDatabase.db"