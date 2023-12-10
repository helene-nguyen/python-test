def setup_module(module):
    """
    Call when importing module
    :param module:
    :return:
    """
    print("\n--> Setup module")


def teardown_module(module):
    """
    Call at the end of tests of module
    :param module: 
    :return: 
    """
    print("--> Teardown module")


class TestClass:
    @classmethod
    def setup_class(cls):
        print("--> Setup class")

    @classmethod
    def teardown_class(cls):
        print("\n--> Teardown class")

    def setup_method(self, method):
        print("\n--> Setup method (for each method called START)")

    def teardown_method(self, method):
        print("--> Teardown method (for each method called END)")

    def test_one(self):
        print("--> Run first test")

    def test_two(self):
        print("--> Run second test")
