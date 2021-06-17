message = "Hello, World! I'm new to programming!"


def write_to_file(file_path, content):
    """write_to_file

    :param file_path: absolute path to the file
    :type file_path: str
    :param content: content to be written to file
    :type: str
    :return: process result
    :rtype: bool
    """
    file_handler = open(file_path, "w")
    file_handler.write(content)
    file_handler.close()


a = 4
b = 5
c = a + b
print(a, b, c)
