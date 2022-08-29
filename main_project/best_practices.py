from time import sleep

print("this is my file to demonstrate best practices.")


def process_data(data):
    print("beginning data processing")
    modified_data = data + " is now modified data"
    sleep(3)
    print("data processing finished")
    return modified_data


def read_data_from_web():
    print("Reading data from the web")
    data = "Data from the web"
    return data


def write_data_to_db(data):
    print("Writing data to a database")
    print(data)


def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_db(modified_data)


if __name__ == "__main__":
    main()
