import re

def split_into_sentences(paragraph):
    """
    Split the paragraph into sentences.
    """

    pattern = r'[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|\s*$)'

    sentences = re.findall(pattern, paragraph)
    return sentences

def display_sentences(sentences):
    """
    Displays each sentence and the total count.
    """
    print("\nIndividual Sentences:\n")

    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence.strip()}")

    print("\nTotal number of sentences:{len(sentences)}")

def main():
    """
    Main function to run the program.
    """
    paragraph = input("Enter a paragraph:\n")
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)

if __name__ == "__main__":
    main()
