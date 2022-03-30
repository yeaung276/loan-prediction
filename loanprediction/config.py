import os

# server configs
port = os.environ.get("PORT", 3000)
host = "0.0.0.0"
log_level = "info"
dev_log_level = "debug"

# authorization config
cookie_name = "session"
