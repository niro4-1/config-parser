def interpolate_env_vars(config):
    import os
    for key, value in config.items():
        if isinstance(value, str):
            config[key] = value.replace('${', 'os.getenv(')
    return config