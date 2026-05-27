
import pandas as pd
data = pd.read_csv('song_finder (1) - song_finder (1) (2).csv')
Rank = data['rank'].tolist()
Song = data['song'].tolist()
Artist = data['artist'].tolist()
Year = data['release_year'].tolist()
Streams = data['streams_billions'].tolist()
Genre = data["genre"].tolist()
Mood = data["mood"].tolist()
Energy = data["energy"].tolist()
history = []
def finder():
    print("Thank you for choosing Song Recommendation")

    genre_input = input("What genre of music would you like to listen to? ").lower()
    mood_input = input("What mood are you in? ").lower()
    energy_input = input("How energetic do you want the song to be? (low, medium, high) ").lower()

    matches = []

    for i in range(len(data)):
        if (genre_input in str(data.loc[i, "genre"]).lower() and
            mood_input in str(data.loc[i, "mood"]).lower() and
            energy_input in str(data.loc[i, "energy"]).lower()):

            matches.append(data.loc[i])

    if matches:
        print("Recommended Song:")
        song = matches[0]
        print(f"{song['song']} by {song['artist']} ({song['release_year']}) with {song['streams_billions']} billion streams.")
        history.append(song['song'])
    else:
        print("No matching song found. Try different preferences.")
def main():
    while True:
        print("Hello! Welcome to Song Finder.")
        print("1. Get a recommendation")
        print("2. View history")
        print("3. Quit")
        try:
            menu = int(input("Choose an option: "))
        except:
            print("Please enter a number.")
            continue
        if menu == 1:
            finder()
        elif menu == 2:
            print("Recommendation History:")
            print(history if history else "No songs yet.")
        elif menu == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
main()
