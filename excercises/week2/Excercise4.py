def main():
    dictionary = {}
    with open("Excercise4.txt", "r") as file:
        words = file.read()
    for word in words.split():
        word = word.lower()
        word = "".join(filter(lambda char: char.isalnum(), word))
        if word not in dictionary:
            dictionary[word] = 1
        else: dictionary[word] += 1

    for (item, value) in dictionary.items():
        print(f"{item}: {value}")
main()