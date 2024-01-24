import os


REPLACE_WORDS = (
    list(os.environ.get("REPLACE_WORDS").split(","))
    if os.environ.get("REPLACE_WORDS")
    else []
)




REPLACE_WORDS=["www 1TamilMV mov", "movies", "Movies", ",", "episode", "Episode", "episodes", "Episodes", "south indian", "South Indian", "web-series", "marathi", "gujrati", "combined", ";", "'", "!", "kro", "jaldi", "bhai", "Audio", "audio", "movi", "language", "Language", "Hollywood", "All", "all", "bollywood", "Bollywood", "South", "south", "hd", "karo", "Karo", "fullepisode", "please", "plz", "Please", "send", "link", "Link", "#request", ":", "full", "Full", "movie", "Movie", "dubb", "dabbed", "dubbed", "gujarati", "season", "Season", "web", "series", "Web", "Series", "webseries", "WebSeries", "upload", "HD", "Hd", "bhejo", "ful", "Send", "Bhejo"]
