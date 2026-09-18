from sqlmodel import create_engine, Session
from os import getenv
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = getenv("SUPABASE_URL")
assert SUPABASE_URL is not None
engine = create_engine(SUPABASE_URL, echo=True)

#  Diferente do Mongoose, que apenas preciso conectar com o
#  banco e fazer as coisas diretamente, nos bancos SQL eu preciso
#  fazer operações a partir de sessões. Uma sessão deve ser inicializada e
#  depois fechada.
#  É isso que a função a seguir já faz, graças ao yield (abrir sessão e fechá-la).


def get_session():
    with Session(engine) as session:
        yield session
