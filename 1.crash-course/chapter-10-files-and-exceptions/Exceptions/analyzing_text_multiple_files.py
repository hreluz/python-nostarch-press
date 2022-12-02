def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        num_words = len(contents.split())
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'moby.txt', 'not-existing.txt']
for filename in filenames:
    count_words(filename)