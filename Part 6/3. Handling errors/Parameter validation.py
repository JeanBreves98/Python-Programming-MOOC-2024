def new_person(name: str, age: int):
    if len(name) == 0 or len(name.split()) <= 1 or len(name) > 40:
        raise ValueError("Invalid input for " + name)
    
    if age < 0 or age > 150:
        raise ValueError("Invalid input for" + str(age))
    else:
        return (name, age)
    
if __name__ == "__main__":
    print(new_person("Jean Moutinho", 25))   # Valid input
    print(new_person(" ", 27))   # Invalid due to name being an empty string
    print(new_person("Jean", 25))   # Invalid due to name containing less than two words
    print(new_person("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 25)) # Invalid due to name being longer than 40 characters
    print(new_person("Victoria", -26))  # Invalid due to age being a negative number
    print(new_person("Dani", 175))  # Invalid due to age being over 150