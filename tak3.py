import random # Importing the random module

# Defining  a class for individual audio files
class Audio:
    def __init__(self, name, url):
        self.name = name          # Name of the audio track
        self.url = url            # URL where the audio can be found
        self.ratings = []         # List to store ratings for this audio track

    def add_rating(self, rating): # Defining a method to add rating
        self.ratings.append(rating)   # Method to add a rating to the list of ratings
        print(f"Added rating {rating} to {self.name}")  # Print a message indicating rating addition

    def get_average_rating(self): # Defining a method to get average rating
        if not self.ratings:# This condition checks if there are any ratings
            print(f"No ratings for {self.name}")   # Print a message if there are no ratings
            return 0 # If no ratings returns 0
        avg_rating = sum(self.ratings) / len(self.ratings)  # Calculate average rating
        print(f"Average rating for {self.name}: {avg_rating}")  # Print average rating
        return avg_rating

# Define a class for playlists
class Playlist:
    def __init__(self, name, genre):
        self.name = name          # Name of the playlist
        self.genre = genre        # Genre of the playlist
        self.audio_files = []     # List to store audio files in the playlist
        self.ratings = []         # List to store ratings for this playlist

    def add_audio_file(self, audio):
        self.audio_files.append(audio)   # Method to add an audio file to the playlist
        print(f"Added {audio.name} to {self.name}")  # Print a message indicating audio addition

    def add_rating(self, rating):
        self.ratings.append(rating)      # Method to add a rating to the list of ratings
        print(f"Added rating {rating} to {self.name}")  # Print a message indicating rating addition

    def get_average_rating(self):
        if not self.ratings:# This condition checks if there are any ratings
            print(f"No ratings for {self.name}")   # Print a message if there are no ratings
            return 0 # If no ratings returns 0
        avg_rating = sum(self.ratings) / len(self.ratings)  # Calculate average rating
        print(f"Average rating for {self.name}: {avg_rating}")  # Print average rating
        return avg_rating

# Define a class for users
class User:
    def __init__(self, name):
        self.name = name   # Name of the user
        print(f"Created user: {self.name}")  # Print a message indicating user creation

# Create users
users = [User("User1"), User("User2"), User("User3")]

# Create audio tracks
audio1 = Audio("Track1", "https://example.com/track1.mp3")
audio2 = Audio("Track2", "https://example.com/track2.mp3")
audio3 = Audio("Track3", "https://example.com/track3.mp3")

# Generate random ratings for audio tracks
for audio in [audio1, audio2, audio3]:
    for user in users:
        audio.add_rating(random.randint(1, 5))  # Add a random rating between 1 and 5 for each user

# Create playlists
playlists = [
    Playlist("Playlist1", "Rock"),
    Playlist("Playlist2", "Pop"),
    Playlist("Playlist3", "Jazz")
]

# Add audio tracks to playlists
for playlist in playlists:
    for audio in [audio1, audio2, audio3]:
        playlist.add_audio_file(audio)  # Add each audio track to each playlist

# Generate random ratings for playlists
for playlist in playlists:
    for user in users:
        playlist.add_rating(random.randint(1, 5))  # Add a random rating between 1 and 5 for each user to each playlist

# Display average ratings
print("Average ratings:")
for audio in [audio1, audio2, audio3]:
    audio.get_average_rating()  # Print average rating for each audio track

for playlist in playlists:
    playlist.get_average_rating()  # Print average rating for each playlist
