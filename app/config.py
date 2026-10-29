import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
load_dotenv()
DB_HOST=os.getenv('DB_HOST','localhost'); DB_PORT=int(os.getenv('DB_PORT','3306')); DB_USER=os.getenv('DB_USER','root'); DB_PASSWORD=os.getenv('DB_PASSWORD','root'); DB_NAME=os.getenv('DB_NAME','baizhan_operation')
DATABASE_URL=f'mysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4'
TORTOISE_ORM={'connections':{'default':DATABASE_URL},'apps':{'models':{'models':['app.models','aerich.models'],'default_connection':'default'}}}
