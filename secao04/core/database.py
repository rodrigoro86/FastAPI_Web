import motor.motor_asyncio
from core.configs import settings


client = motor.motor_asyncio.AsyncIOMotorClient(settings.DB_URL)
db = client.analise_desempenho
#db = client.analise_desempenho_test
