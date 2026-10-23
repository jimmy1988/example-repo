#List all the movies
favourite_movies = [
    "The Imitation Game",
    "The Devil Wears Prada",
    "Priscilla, Queen Of the Desert",
    "Avengers: End Game",
    "The Help"
]

#Initialize the index
index = 1

#loop around the movies list
for movie in range(len(favourite_movies)):
    print(f"Movie {index}: {favourite_movies[movie]}") #print each movie out in a formatted string
    index += 1 #increment the index by 1