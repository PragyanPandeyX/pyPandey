
import sys
import os

class Var:
    # Mandatory configurations
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else 20348897
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else "ecfb9a700b8398caf58c53f36ccf5b06"
    )
    SESSION = (
        sys.argv[3] if len(sys.argv) > 3 
        else "BQE2f-EACfbwubzRBTsNMBEjZ7LxEateLwOimujk-kPaeiLGt1hgQJngckWG3LVm3UjlPFiOOF39kD0SS-3oeMkUmoiYOXg99eJuywiagk2TmRVd_yHPpaxhf_iabR8Q4sjGjy2ByiKUJU3jp3jI90fqoywckNdENn_EVudx0vvZ7tAYIuI1-U8L691Yd22aeLg3GkQwVVJ22Jq760zsAyKH8eecYEgM3kA7L_PHk4phoVLym0eIuWC7a4KmqQBcrTD4-VeN7gsQsA8omnjlKu7pDsvUEjrwVOIyeUPC_B3IDWRHXX0eSZOwDeoKOGPrOWkaRkNQkE9pomPOodeUUOVYaDw8TwAAAAHdPGQXAA"
    )
    REDIS_URI = (
        sys.argv[4] if len(sys.argv) > 4 else None  # Set a default if you have one
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else None  # Set a default if you have one
    )

    # Extras
    
    LOG_CHANNEL = -1002377046364  # Set log channel here
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API = os.environ.get("HEROKU_API")
    VC_SESSION = os.environ.get("VC_SESSION")
    ADDONS = os.environ.get("ADDONS", 'True').lower() in ['true', '1']
    VCBOT = os.environ.get("VCBOT", 'False').lower() in ['true', '1']
    
    # For Railway
    REDISPASSWORD = os.environ.get("REDISPASSWORD")
    REDISHOST = os.environ.get("REDISHOST")
    REDISPORT = os.environ.get("REDISPORT")
    REDISUSER = os.environ.get("REDISUSER")
    
    # For SQL
    DATABASE_URL = os.environ.get("DATABASE_URL")
    
    # For MongoDB
    MONGO_URI = "mongodb+srv://AvyukthX:AvyukthX@bot.ctdiudr.mongodb.net/?retryWrites=true&w=majority"

# Example usage
if __name__ == "__main__":
    print(f"API_ID: {Var.API_ID}")
    print(f"API_HASH: {Var.API_HASH}")
    print(f"SESSION: {Var.SESSION}")
    print(f"BOT_TOKEN: {Var.BOT_TOKEN}")
    print(f"MONGO_URI: {Var.MONGO_URI}")
