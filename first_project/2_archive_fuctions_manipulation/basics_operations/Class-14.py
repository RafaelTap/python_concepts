def main():
    print("type your frases, type exit to stop and save archive.")
    phrases = []
    while True:
        entry = input("-> ")
        if entry.lower() == "exit":
            break
        phrases.append(entry)

    with open("archive_0_1.txt", 'w') as archive:
        for phrase in phrases:
            archive.write(phrase + "\n")

    print("original archive created, let's manipulate it !")
    modified_data = []
    with open("archive_0_1.txt", 'r') as archive:
        for line in archive:
            modified_data.append(line.strip().upper()) #converting to upper case.

    with open("archive_0_1.txt", 'w') as archive:
        for line in modified_data:
            archive.write(line + "\n")

    print("archive modified")

if __name__ == "__main__":
    main()