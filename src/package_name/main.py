"""
main.py
====================================
The core module of my example project
"""


def main() -> None:
    """
	Print to console
	"""
    print('Hello from my package!')


class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name):
        """
		Blah blah blah.
		Parameters
		---------
		name
		    A string to assign to the `name` instance attribute.
		"""
        self.name = name

    def about_self(self):
        """
		Return information about an instance created from ExampleClass.
		"""
        return 'I am a very smart {} object.'.format(self.name)

