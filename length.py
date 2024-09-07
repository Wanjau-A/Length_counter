def main():
    input_text = input("Text: ").strip()
    input_text_length = len(input_text)
    print(input_text_length)
    
def compute_length(input_text):
    length = 0
    for character in input_text:
        length = length + 1
    return length

if __name__ == "__main__":
    main()


