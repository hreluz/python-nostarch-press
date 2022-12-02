try:
    with open('nofile-txt') as f:
        contents = f.read()
except FileNotFoundError:
    pass
