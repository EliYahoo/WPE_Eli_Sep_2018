# Context managers - deal with resource deallocation
# two ways to implement - __enter__(), __exit__() functions
# or a function with decorator @contextmanager, with exactly one yield all that's before the yield is
# the equivalent of __enter__() and after __exit__()

class Tee:

    def __init__(self, *args):
        self.files = args

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for file in self.files:
            file.close()

    def write(self, text):
        print(text)
        for file in self.files:
            file.write(text)

    def writelines(self, texts):
        for text in texts:
            print(text)
            for file in self.files:
                file.write(text)