def count_words(text):
    words = text.split()
    return len(words)

def count_text(option):

    if option == "WT":
        your_text = input("Please insert your text: ")
        count_word = count_words(your_text)
        print(f"Number of words: {count_word}")

    elif option == "RM":
        while True:
            select_your_text = input("please select text (for example example.txt): ")
            try:
                with open(f"{select_your_text}", 'r') as file:
                    text = file.read()
                count_word = count_words(text)
                print(f"Number of words: {count_word}")
                break
            except FileNotFoundError:
                print("File not found!")
                continue

def main():
    while True:
        answer = input("Do you want to write the text yourself or do you have a ready-made text [WT|RM]? ")

        if answer.upper() == "WT":
            count_text("WT")
        elif answer.upper() == "RM":
            count_text("RM")
        else:
            print("Invalid option. Please choose either 'WT' or 'RM'.")
            continue

        continue_end = input("Do you want to continue or not[Y|N]? ")
        if continue_end.capitalize() == "Y":
           continue
        elif  continue_end.capitalize() == "N":
            print("Thank you for using the word counting tool. Goodbye!")
            break
        else:
            break

if __name__ == "__main__":
    print("Hello, welcome! This tool helps you count the number of words in a text.")
    main()