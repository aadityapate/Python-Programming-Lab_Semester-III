# i. Add a new movie

movie = {"Taare Zameen Par": 12, "3 Idiots": 3, "Yeh Jawani Hai Deewani": 6}
print("\nMovie Timings: ", movie)

movie["Chhichhore"] = 9
print("\nAfter Releasing of new movie: ", movie)

# ii. Display movies available at 9 pm

print("\nMovies @9PM: ", list(movie.keys())
[list(movie.values()).index(9)])

# iii. Remove the details of the specific movie

movie.pop('Taare Zameen Par')
print("\nAfter Cancelling Taare Zameen Par: ", movie)

# iv. Remove the last movie details

movie.popitem()
print("\nAfter Removing the Details of last Movie: ", movie, "\n")
