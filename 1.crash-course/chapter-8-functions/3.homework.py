def city_country(city, country):
    return f"{city}, {country}"


print(city_country('Santiago', 'Chile'))


def make_album(artist_name, album_title, number_songs=None):
    music = {'artist': artist_name, 'album': album_title}

    if number_songs:
        music['songs'] = number_songs

    return music


while True:
    print('\n Please enter the artist name: ')
    print("(enter 'q' at any time to quit)")
    artist = input('Artist name: ')

    if artist == 'q':
        break

    print('\n Please enter the album name: ')
    print("(enter 'q' at any time to quit)")
    album = input('Album name: ')

    if artist == 'q':
        break

    print(f"Hello, your json is {make_album(artist, album)}")