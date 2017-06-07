if __name__ == '__main__':

    import unittest

    all_tests = unittest.TestLoader().discover('.', pattern='test_*.py')
    unittest.TextTestRunner().run(all_tests)
