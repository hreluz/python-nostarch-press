def read_names(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        # print(f"The file {filename} was not found")
        pass


read_names('cats.txt')
read_names('dogs.txt')
read_names('parrots.txt')
