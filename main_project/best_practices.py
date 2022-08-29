from time import sleep

print("this is my file to demonstrate best practices.")


def process_data(data):
    print("beginning data processing")
    modified_data = data + " modified data"
    sleep(3)
    print("data processing finished")
    return modified_data
