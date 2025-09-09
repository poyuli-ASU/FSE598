import json                                                             # Import the json module for JSON formatting
import urllib.request                                                   # Import requests module to fetch file from GitHub if needed
import os                                                               # Import os module to check file existence
import xml.etree.ElementTree as ET                                      # Import XML module for XML generation

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
        return {"Movie": result}                                        # Return the Movie object

# Read the file and create Movie objects, and return a list of Movie objects
def read_movies(filename):
    movies = []
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    # Check if the file exists locally; if not, fetch from GitHub
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
    else:
        try:
            github_url = "https://raw.githubusercontent.com/poyuli-ASU/FSE598/main/Module2HW3/Movies.txt"
            print(f"Trying to access: {github_url}")
            with urllib.request.urlopen(github_url) as response:
                content = response.read().decode('utf-8').strip()
        except urllib.error.HTTPError as e:
            print(f"HTTP Error {e.code}: {e.reason} - GitHub repository or file may not exist")
            return []
        except Exception as e:
            print(f"Error accessing GitHub: {e}")
            return []

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

# Create Movies.json file at current directory
def create_movies_json(list_movies, output_filename='Movies.json'):
    
    script_dir = os.path.dirname(os.path.abspath(__file__))             # Get the directory where this script is located
    file_path = os.path.join(script_dir, output_filename)
    
    with open(file_path, 'w', encoding='utf-8') as json_file:           # Write the JSON data to Movies.json file
        json.dump(list_movies, json_file, indent=2, ensure_ascii=False) # Write the final JSON list of movies to file
    print(f"Movies data has been written to {output_filename}")

# Generate a sorting method for Movie.json file
def sort_movies_by_attr(attr):

    script_dir = os.path.dirname(os.path.abspath(__file__))                        # Get the directory where this script is located
    file_path = os.path.join(script_dir, 'Movies.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:                      # Open the Movies.json file for reading
            movies = json.load(json_file)                                              # Load the JSON data from Movies.json file
        
        sorted_movies = []
        match attr:
            case 'Title':
                sorted_movies = sorted(movies, key=lambda x: x['Movie'][0]['Title'])   # Sort movies by the 'Title' attribute
            case 'Genre':
                sorted_movies = sorted(movies, key=lambda x: x['Movie'][1]['Genre'])   # Sort movies by the 'Genre' attribute
            case 'Director':
                sorted_movies = sorted(movies, key=lambda x: x['Movie'][2]['Director']['Name'])  # Sort movies by the first 'Director' name
            case 'Studio':
                sorted_movies = sorted(movies, key=lambda x: x['Movie'][-2]['Studio']) # Sort movies by the 'Studio' attribute
            case 'Year':
                sorted_movies = sorted(movies, key=lambda x: x['Movie'][-1]['Year'])   # Sort movies by the 'Year' attribute

        create_movies_json(sorted_movies, output_filename=f'MoviesSorted.json') # Create sorted Movies JSON file
    
        print(f"Movies data has been sorted by {attr} and written to MoviesSorted.json")
    except FileNotFoundError:
        print("Movies.json file not found. Please create it first.")
    return []

# Convert Sorted JSON file to XML format
def XmlGeneration(sorted_json_file, output_xml_file):
    script_dir = os.path.dirname(os.path.abspath(__file__))         # Retrieve the directory of the current script
    file_path = os.path.join(script_dir, sorted_json_file)          # Create the full file path
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:   # Open and read the JSON file
            movies = json.load(json_file)                           # Load the JSON data

        root = ET.Element("Movies")                                 # Create the XML root element
        for movie_data in movies:                                   # Iterate through each movie data
            movie_elem = ET.SubElement(root, "Movie")               # Create a Movie element for each movie

            for item in movie_data['Movie']:                        # Iterate through each attribute of the movie
                for key, value in item.items():                     # Process each key-value pair of the attribute
                    if key == 'Director':                           # Special handling for Director attribute
                        director_elem = ET.SubElement(movie_elem, "Director")  # Create Director element
                        name_elem = ET.SubElement(director_elem, "Name")       # Create Name element inside Director
                        name_elem.text = value['Name']              # Set the director name as the Name element content
                    else:                                           # Process other attributes (Title, Genre, Studio, Year)
                        elem = ET.SubElement(movie_elem, key)       # Create corresponding XML element
                        elem.text = str(value)                      # Set the attribute value as the element content

        
        ET.indent(root, space="  ", level=0)                       # Add indentation to XML elements
        tree = ET.ElementTree(root)                                 # Create the XML tree structure
        tree.write(os.path.join(script_dir, output_xml_file), encoding='utf-8', xml_declaration=True)  # Write to XML file
        print(f"XML data has been written to {output_xml_file}")    # Display success message
    except FileNotFoundError:                                       # Handle file not found error
        print(f"{sorted_json_file} not found.")
    except Exception as e:                                        
        print(f"Error occurred: {e}")


# The main program
def main():
    #Question 2 - Read Movies.txt file and create Movies.json file
    movies = read_movies('Movies.txt')                   # Read file and get list of Movie objects
    list_movies= []
    for movie in movies:                                 # Print each movie in JSON format
        json_data = movie.to_json_format()
        list_movies.append(json_data)
    print("Movie = ")
    print(json.dumps(list_movies, indent=2, ensure_ascii=False))    # print the final JSON list of movies
    create_movies_json(list_movies)                      # Create Movies.json file

    # Question 3 - Sort Movies.json file by different attributes and create Sorted_Movies_by_<Attribute>.json files
    #attributes = ['Title', 'Genre', 'Director', 'Studio', 'Year']
    #for attr in attributes:
    #    sort_movies_by_attr(attr)                        # Sort movies by each attribute and create corresponding JSON file
    sort_movies_by_attr('Director')                      # default sorting by Director

    # Question 4 - Convert Sorted JSON files to XML format
    default_converted_file_name = 'MoviesSorted.json'   # Default using Director_sorted to convert to XML
    XmlGeneration(default_converted_file_name, f'Movies.xml')

# 認定主程式並執行
if __name__ == "__main__":
    main()