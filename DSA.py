def count_chars(text):
    count = 0
    for char in text:
        count +=1
        return count
def main():
    text = input("enter name:")
    print("characters count:", count_chars(text))
main()