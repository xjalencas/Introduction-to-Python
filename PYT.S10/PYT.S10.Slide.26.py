class MyError(Exception):

    """My defined exception"""

    def __init__(self, value):
        self.value = value
        super().__init__(f"Incorrect assigned value: {value}")


e = MyError(23)
print(e)

raise e
