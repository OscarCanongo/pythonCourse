import random

songs = ["Fragilidad - Rubytates",
        "Caja de madera - Lng Sht",
        "El rey del barrio - Los chotgun",
        "No dejes que - Caifanes",
        "Dos mundos - Reyno",
        "Fantasmas - Serbia",
        "Paseo Sideral - Costera",
        "Mis Anacronismos (Y los tuyos) - Andrés Canalla",
        "Cosmos - Surfistas del sistema"]

random_song = random.choice(songs)

print(f"You must listen to this song: {random_song}")
