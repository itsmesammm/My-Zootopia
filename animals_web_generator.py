import json

def load_data(file_path):
    with open(file_path, 'r') as handle:
        return json.load(handle)

def print_animals_data(animal):
    print("Name: ", animal["name"])
    print("Diet:", animal['characteristics'].get('diet', 'N/A'))
    print("Location: ", animal["locations"][0])
    print("Type:", animal['characteristics'].get('type', 'N/A'))
    print("\t")

animals_data = load_data('animals_data.json')

def main():
    for animal in animals_data:
        print_animals_data(animal)

if __name__ == "__main__":
    main()
