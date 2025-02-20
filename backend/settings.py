#from envparse import Env

#database url sqlyt3 + aiosqlite
REAL_DATABASE_URL = "sqlite+aiosqlite://db.db"

#Postgres database 
# REAL_DATABASE_URL = env.str(
#     "REAL_DATABASE_URL",
#     default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres",
# )

#port of uvicorn
APP_PORT = 8080
#APP_PORT = env.int("APP_PORT")

# SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
# ALGORITHM: str = env.str("ALGORITHM", default="HS256")
# ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
# SENTRY_URL: str = env.str("SENTRY_URL")

# # test envs
# TEST_DATABASE_URL = env.str(
#     "TEST_DATABASE_URL",
#     default="postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5433/postgres_test",
# )  # connect string for the test database

#Web-site 999.md urls
BASE_URL = "https://999.md/"
GRAPHQL_BASE_URL = "https://999.md/graphql"