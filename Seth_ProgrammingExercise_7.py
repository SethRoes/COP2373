import re

def get_paragraph_input():
    print("Please enter your paragraph. Press Enter twice to finish input.")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return " ".join(lines)

def analyze_paragraph(paragraph):

    sentences = re.split(r'(?<=[.!?])\s*(?=[A-Z0-9])', paragraph)

    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences, len(sentences)

def main():
    paragraph_text = get_paragraph_input()
    individual_sentences, sentence_count = analyze_paragraph(paragraph_text)

    print("\n--- Individual Sentences ---")
    for i, sentence in enumerate(individual_sentences):
        print(f"{i+1}. {sentence}")

    print(f"\nTotal number of sentences: {sentence_count}")

if __name__ == "__main__":
    main()