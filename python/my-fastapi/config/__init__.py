from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,  # enable layerd environments on files
    load_dontenv=True,  # support python-dotenv to load .env files
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
