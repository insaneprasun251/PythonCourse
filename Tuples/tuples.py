# t = "a", "b", "C"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))


welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightfight", "Budgie", 1981
# Tuple inside a list
imelda = "More Mayhem", "Emilda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), \
         (4, "Kentish Town Waltz"))

metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])

# Changing a tuple by an assignment
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)

metallica2 = ["Ride the Lightning", "Metallica", 1984]

# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)
#
# title, artist, year = metallica2
# print(title)
# print(artist)
# print(year)
#
# print(imelda)
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# '\t' creates a tab indentation
title, artist, year, tracks = imelda
print(title, artist, year)
for song in tracks:
    track, title = song
    print('\tTrack number {}, Title: {}'.format(track, title))
