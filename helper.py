import _mysql

def formatDateTime(input):
    arr = input.split('/')
    return f'20{arr[2]}-{arr[0]}-{arr[1]}'

#### DO NOT CHANGE ####
if __name__ == "__main__":
    exit(1)