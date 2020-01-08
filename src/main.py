from eve import Eve

from src.config.vars import (
    MONGO_DATABASE,
    MONGO_HOST,
    MONGO_PASSWORD,
    MONGO_PORT,
    MONGO_USER,
)

my_settings = dict(
    DOMAIN={"groceryoffer": {}, "herbvuoffer": {}, "mpnoffer": {}},
    # Read only
    RESOURCE_METHODS=["GET"],
    PUBLIC_METHODS=["GET"],
    ITEM_METHODS=["GET"],
    PUBLIC_ITEM_METHODS=["GET"],
    # Let's just use the local mongod instance. Edit as needed.
    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST=MONGO_HOST,
    MONGO_PORT=int(MONGO_PORT),
    # Skip this block if your db has no auth. But it really should.
    MONGO_USERNAME=MONGO_USER,
    MONGO_PASSWORD=MONGO_PASSWORD,
    # Name of the database on which the user can be authenticated,
    # needed if --auth mode is enabled.
    MONGO_AUTH_SOURCE="admin",
    MONGO_DBNAME=MONGO_DATABASE,
    ALLOW_UNKNOWN=True,  # Show all fields instead of relying on schema specification
    RENDERERS=["eve.render.JSONRenderer"],
)

app = Eve(settings=my_settings)

if __name__ == "__main__":
    app.run()
