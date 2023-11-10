#This module is imported to ch8_ex0.py

#Function definitions:
def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

def make_album(artist, album, songs=None):
    """Creates a dictionary from artist+album using optional argument <songs> and special value None"""
    work = {'artist' : artist, 'album' : album}
    if songs:
        work['songs'] = songs
    return work

