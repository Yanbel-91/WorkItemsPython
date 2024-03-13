import unittest
from src.Exercises import Exercises


class ExercisesTest(unittest.TestCase):
    def test_exercise_one(self):
        self.assertFalse(Exercises.exercise_one("test"))
        self.assertTrue(Exercises.exercise_one("racecar"))
        self.assertTrue(Exercises.exercise_one("anna"))
        self.assertFalse(Exercises.exercise_one("hello"))
        self.assertFalse(Exercises.exercise_one("bierkasten"))
        self.assertTrue(Exercises.exercise_one("lagerregal"))
        self.assertTrue(Exercises.exercise_one("annahetztehanna"))
        self.assertTrue(Exercises.exercise_one("ebbe"))

    def test_exercise_two(self):
        self.assertEqual(Exercises.exercise_two(3), "Fizz")
        self.assertEqual(Exercises.exercise_two(5), "Buzz")
        self.assertEqual(Exercises.exercise_two(15), "FizzBuzz")
        self.assertEqual(Exercises.exercise_two(7), "7")

    def test_exercise_three(self):
        self.assertEqual(Exercises.exercise_three(["b", "a", "c"]), ["a", "b", "c"])

    def test_exercise_four(self):
        self.assertTrue(Exercises.exercise_four("listen", "silent"))
        self.assertFalse(Exercises.exercise_four("hello", "world"))
        self.assertTrue(Exercises.exercise_four("a gentleman", "elegant man"))
        self.assertTrue(Exercises.exercise_four("the morse code", "here come dots"))
        self.assertTrue(Exercises.exercise_four("the eyes", "they see"))

    def test_exercise_five(self):
        self.assertEqual(Exercises.exercise_five([3, 1, 7, 4, 9]), 9)
        self.assertEqual(Exercises.exercise_five([-3, -1, -7, -4, -9]), -1)
        self.assertEqual(Exercises.exercise_five([0]), 0)

