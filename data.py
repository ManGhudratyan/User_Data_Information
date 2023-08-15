def write_data_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write("Name Surname Age Profession\n");
        for info in data:
            name = info['name'];
            surname = info['surname'];
            age = info['age'];
            profession = info['profession'];
            line = f"{name} {surname} {age} {profession}\n";
            file.write(line);
            
def sort_data(data, key_function, newFileName):
    sorted_data = sorted(data, key = key_function);
    write_data_to_file(sorted_data, newFileName);

def main():
    data = [
        {'name': 'Mane', 'surname': 'Ghazaryan', 'age': 20, 'profession': 'programmer'},
        {'name': 'Arpi', 'surname': 'Isahakyan', 'age': 18, 'profession': 'singer'},
        {'name': 'Sargis', 'surname': 'Manukyan', 'age': 25, 'profession': 'teacher'},
        {'name': 'Tigran', 'surname': 'Hakobyan', 'age': 36, 'profession': 'hairdresser'},
        {'name': 'Hovhannes', 'surname': 'Barseghyan', 'age': 48, 'profession': 'driver'},
        {'name': 'Van', 'surname': 'Sahakyan', 'age': 26, 'profession': 'writer'}
    ];
    
    filename = "data.txt";
    user_choice = input('Sort by name, surname, age or profession?: ');
    
    if (user_choice == 'name'):
        newFileName = "sorted_by_name.txt";
        sorted_data = sorted(data, key = lambda x : x['name']);
    elif (user_choice == 'surname'):
        newFileName = "sorted_by_surname.txt";
        sorted_data = sorted(data, key = lambda x : x['surname']);
    elif (user_choice == 'age'):
        newFileName = "sorted_by_age.txt";
        sorted_data = sorted(data, key = lambda x : x['age']);
    elif (user_choice == 'profession'):
        newFileName = "sorted_by_profession.txt";
        sorted_data = sorted(data, key = lambda x : x['profession']);
    else:
        print('Please write only name, surname, age and profession.')
        return  

    sort_data(sorted_data, lambda x : x[user_choice], newFileName)
main();
