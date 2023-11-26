import streamlit as st
import os

# Define the recipe pages with an optional serving size parameter and image
def recipe(name, weeks=1, numshows=0):
    st.title("Here are some anime you can watch from the " + name.lower() + " genre") #1st New Stremalit Methods
    #image_filename = os.path.join("images/"+name.lower() + ".jpg") #Will Include 3 Images
    #st.image(image_filename, use_column_width=True)
    st.image(name + ".jpeg", use_column_width=True)
    st.header("Selected from a list of 30+ fantastic shows...")

    animeList = {"Attack on Titan":[["Action","Sad"], 89], "Naruto":[["Action","Comedy"],720], "One Piece":[["Action","Adventure","Comedy"],1083], 
    "Beastars":[["Drama","Mystery"],22], "Death Note":[["Drama","Mystery"],37], "Bleach":[["Action","Fantasy"],366], "Parasite The Maxim":[["Drama","Horror","Action"],24], 
    "One Punch Man":[["Action","Comedy"],24], "Dr Stone":[["Science","Comedy"],57], "Cells at Work":[["Science","Comedy"],21], "JoJos Bizzare Adventure":[["Action","Comedy","Adventure"], 190],
    "Dragon Ball":[["Action","Adventure"],798], "Berserk":[["Fantasy","Adventure","Horrror","Sad"],26], "Corpse Party":[["Horror"],4], "Made in Abyss":[["Adventure","Horror"],27],
    "Hunter X Hunter":[["Action","Adventure"],148], "Terra Formars":[["Horror","Action","Science"],13], "Full Metal Alchemist: Brotherhood":[["Action","Science Fiction"], 64], 
    "Cyberpunk: Edgerunners":[["Science Fiction","Action"], 10], "Tokyo Ghoul":[["Action","Drama"],48], "Mob Psycho 100":[["Action","Slice of Life","Comedy"],36], 
    "Spy X Family":[["Action","Slice of Life"], 24], "Dororo":[["Action","Fantasy","Sad"], 26], "To Your Eternity":[["Adventure","Fantasy","Sad"],40], "Vinland Saga":[["Action","Adventure"], 48],
    "Fairy Tail":[["Fantasy","Action"],328], "Jujutsu Kaisen":[["Action","Fantasy"], 48], "My Hero Academia":[["Action","Comedy"], 113], "Demon Slayer":[["Action", "Fantasy", "Adventure"], 49],
    "Gurren Lagann":[["Science Fiction","Action","Adventure"],27], "Psycho-Pass":[["Science Fiction","Mystery"],41], "Promised Neverland":[["Horror","Mystery"],12,], 
    "Seven Deadly Sins":[["Fantasy","Action"],100], "Samurai Champloo":[["Adventure","Comedy"],52], "Junji Ito Collection":[["Horror"],12], "Another":[["Horror","Drama"],12],
    "Kabenari of the Iron Fortress":[["Action","Horror"],12]}
    
    for anime in animeList:
        genres = animeList[anime][0]
        episodes = animeList[anime][1]
        if name in genres and episodes/35 <= weeks:
            numshows += 1
            st.write(anime)
    if numshows == 0:
        st.header("Sorry, theres no shows for you at the time. Please select again.")
    




# Create navigation sidebar
st.sidebar.title("What are you intrested in?")
your_genre = st.sidebar.radio("Whats your favorite genre", ["Adventure","Action","Comedy","Slice of Life","Horror","Drama","Fantasy","Mystery","Science Fiction","Science","Sad"])#2nd New Streamlit Method

# Number of weeks you're willing to sit through a show for.
weeks = st.sidebar.number_input("How many weeks do you plan on bingeing", min_value=1, value=1)#3rd Method

# 
if your_genre == "Adventure":
    recipe("Adventure", weeks, 0)
elif your_genre == "Action":
    recipe("Action", weeks, 0)
elif your_genre == "Comedy":
    recipe("Comedy", weeks, 0)
elif your_genre == "Slice of Life":
    recipe("Slice of Life", weeks, 0)
elif your_genre == "Horror":
    recipe("Horror", weeks, 0)
elif your_genre == "Drama":
    recipe("Drama", weeks, 0)
elif your_genre == "Fantasy":
    recipe("Fantasy", weeks, 0)
elif your_genre == "Mystery":
    recipe("Mystery", weeks, 0)
elif your_genre == "Science":
    recipe("Science", weeks, 0)
elif your_genre == "Science Fiction":
    recipe("Science Fiction", weeks, 0)
elif your_genre == "Sad":
    recipe("Sad", weeks, 0)
