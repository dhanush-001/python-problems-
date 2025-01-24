def is_valid_ipv4(ip):
    parts =ip.split(".")
    return len(parts)==4 and all(part.isdigit() and 0<=int(part) <=255 for part in parts)

print(is_valid_ipv4("193.170.150.33"))
