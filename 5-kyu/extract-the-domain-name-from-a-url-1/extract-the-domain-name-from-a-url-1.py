def domain_name(url):
    # Step 1: Remove scheme
    if "://" in url:
        url = url.split("://")[1]
​
    # Step 2: Remove www.
    if url.startswith("www."):
        url = url[4:]
​
    # Step 3: Get domain before first dot
    return url.split('.')[0]
​