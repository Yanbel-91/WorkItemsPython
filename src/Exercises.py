class Exercises:
    @staticmethod
    def exercise_one(word: str) -> bool:
        """
        PALINDROME CHECK
        Write a function that checks whether a given string is a palindrome (reads the same forwards and backwards).
        This function should not be case-sensitive.
        """
        return False

    @staticmethod
    def exercise_two(number: int) -> str:
        """
        FIZZBUZZ
        Write a program that returns the given number,
        but for multiples of three, return "Fizz" instead of the number,
        and for the multiples of five, return "Buzz". For numbers that
        are multiples of both three and five, return "FizzBuzz".
        """
        return "0"

    @staticmethod
    def exercise_three(unsorted_list: list) -> list:
        """
        SORTING ALGORITHM
        Write a sorting algorithm to sort a list of strings in ascending order
        without using any built-in functions.
        Please focus on stability, cost efficiency, and low memory consumption.
        """
        return unsorted_list

    @staticmethod
    def exercise_four(word_one: str, word_two: str) -> bool:
        """
        ANAGRAM CHECK
        Write a function to check if two strings are anagrams of each other
        (contain the same characters in a different order).
        This function should not be case-sensitive.
        """
        return word_one == word_two

    @staticmethod
    def exercise_five(numbers: list) -> int:
        """
        FIND MAXIMUM
        Write a function that finds the maximum number in a list of integers
        without using any built-in functions or sorting algorithms.
        """
        return numbers[1]
