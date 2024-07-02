# import unittest
# from method_override import Adult, Child

# class TestAdult(unittest.TestCase):

#     def setUp(self) -> None:
#         # Arrange
#         person = Adult("Jess", 20, "blue", "red")

#     def test_giving_full_details(self):
#         # Act
#         person = Adult("Jess", 20, "blue", "red")
#         # Assert
#         self.assertEqual(person.age, 20)
 

#     def test_method_override(self):
#         person = Adult("Jess", 20, "blue", "red")
#         self.assertEqual(person.can_drive(), "Is old enough to drive.)")  


# class TestChild(unittest.TestCase):

#     def setUp(self) -> None:
#         # Arrange
#         child = Child("Lwandile", 14, "green", "yellow")

#     def test_giving_full_details(self):
#         # Act
#         child = Child("Lwandile", 14, "green", "yellow")
#         # Assert
#         self.assertEqual(child.age, 14)

#     def test_method_override(self):
#         child = Child("Lwandile", 14, "green", "yellow")
#         self.assertEqual(child.can_drive(), "Is to young to drive.")


# if __name__ == "__main__":  
#         unittest.main()


import unittest
from method_override import Adult, Child

class TestAdult(unittest.TestCase):

    def setUp(self) -> None:
        # Arrange
        person = Adult("Jess", 20, "blue", "red")

    def test_giving_full_details(self):
        # Act
        person = Adult("Jess", 20, "blue", "red")
        # Assert
        self.assertEqual(person.age, 20)

    # def test_method_override(self):
    #     person = Adult("Jess", 20, "blue", "red")
    #     self.assertTrue(Adult.can_drive())  


class TestChild(unittest.TestCase):

    def setUp(self) -> None:
        # Arrange
        child = Child("Lwandile", 14, "green", "yellow")

    def test_giving_full_details(self):
        # Act
        child = Child("Lwandile", 14, "green", "yellow")
        # Assert
        self.assertEqual(child.age, 14)

    def test_method_override(self):
        child = Child("Lwandile", 14, "green", "yellow")
        self.assertFalse(child.can_drive())  

if __name__ == "__main__":
    unittest.main()
