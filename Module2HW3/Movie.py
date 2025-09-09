import json                                                             # Import the json module for JSON formatting
import urllib.request                                                   # Import requests module to fetch file from GitHub if needed
import os                                                               # Import os module to check file existence

# Define the Movie class
class Movie:
    def __init__(self, title, genre, directors, studio, year):          # Constructor to initialize movie attributes
        self.title = title
        self.genre = genre
        self.directors = directors                                      # List of directors
        self.studio = studio
        self.year = year
    
    def to_json_format(self):                                           # Adding the attributes to JSON value format   
        result = [
            {"Title": self.title},
            {"Genre": self.genre}
        ]
        for director in self.directors:
            result.append({"Director": {"Name": director}})
        result.extend([
            {"Studio": self.studio},
            {"Year": self.year}
        ])
        return result

# Read the file and create Movie objects, and return a list of Movie objects
def read_movies(filename):
    movies = []
    # Check whether the file exists in the current directory, or read the file in the GitHub repository 
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
    else:  # Read from GitHub if local file not found
        github_url = "https://raw.githubusercontent.com/poyuli-ASU/FSE598/main/Module2HW3/Movies.txt"
        with urllib.request.urlopen(github_url) as response:
            content = response.read().decode('utf-8').strip()

    movie_sperated = content.split('\n\n')                          # Split the content into different movies string     

    for block in movie_sperated:                                    # Process each movie string
        lines = block.strip().split('\n')                           # Getting lines(attributes) one by one
        title = genre = studio = year = None                        # Initialize variables
        directors = []                                              # Initialize directors list

        for line in lines:
            if line.startswith('Title: '):                          # Check if the line starts with 'Title: ' > Extract title  
                title = line[7:]                                    # Setting value : after 'Title: ' is character index 7 to end
            elif line.startswith('Genre: '):                        # Check if the line starts with 'Genre: ' > Extract genre
                genre = line[7:]                                    # Setting value : after 'Genre: ' is character index 7 to end
            elif line.startswith('Director Name: '):                # Check if the line starts with 'Director Name: ' > Extract director name
                directors.append(line[15:])                         # Setting value : after 'Director Name: ' is character index 15 to end
            elif line.startswith('Studio: '):                       # Check if the line starts with 'Studio: ' > Extract studio
                studio = line[8:]                                   # Setting value : after 'Studio: ' is character index 8 to end
            elif line.startswith('Year: '):                         # Check if the line starts with 'Year: ' > Extract year
                year = int(line[6:])                                # Setting value : after 'Year: ' is character index 6 to end and convert to integer

        if title and genre and directors and studio and year:
            movies.append(Movie(title, genre, directors, studio, year)) # Create Movie object and add to list
    
    return movies                                                       # Return the list of Movie objects  
# The main program
def main():
    movies = read_movies('Movies.txt')                   # Read file and get list of Movie objects
    for movie in movies:                                 # Print each movie in JSON format  
        json_data = movie.to_json_format()
        print(json.dumps(json_data, indent=2, ensure_ascii=False))

# 認定主程式並執行
if __name__ == "__main__":
    main()