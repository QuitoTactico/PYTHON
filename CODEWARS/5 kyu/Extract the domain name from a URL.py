def domain_name(url: str):
    url = url.replace("www.", "")

    for _ in range(2):
        last_dot = url.rfind(".")
        if last_dot != -1:
            url = url[:last_dot]

    http = url.find("://")
    if http != -1:
        url = url[http + 3 :]

    return url


print(domain_name("http://www.zombie-bites.com"))

# ------------------------- smart one --------------------------


def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
