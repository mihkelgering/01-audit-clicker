def is_config_valid(config):
    if not config:
        return False
    if not "nickname" in config:
        print("Nickname is missing")
        return False
    if not "pw" in config:
        print("Password is missing")
        return False
    if not "chromedriver_path" in config:
        print("Chromedriver path is missing")
        return False
    if not "audit_url" in config:
        print("Audit URL is missing")
        return False
    if not "audit_code" in config:
        print("Audit code is missing")
        return False
    return True
