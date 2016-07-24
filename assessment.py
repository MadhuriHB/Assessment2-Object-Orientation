"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   
   1. Encapsulation:

        It means hiding data.
        In an object oriented python program, you can restrict access to
        methods and variables through Encapsulation.
        This can prevent the data from being modified
        by accident.
        Abstracton is achieved through Encapsulation.


    2. Inheritance:

        The transfer of the characteristics of a class to 
        other classes that are derived from it.


    3. Polymorphism:

        In a child class we can change how some methods work whilst keeping
        the same name. We call this polymorphism and it is useful because
        we do not want to keep introducing new method names for 
        functionality that is pretty similar in each class. 

2. What is a class
   Class can be thought of as blueprint for creating objects.



3. What is an instance attribute?
   Instance attributes are owned by the specific instances of a class.
   This means for two different instances the instance attributes are 
   usually different. 


4. What is a method?
   Methods are functions defined within the class.

        A method differs from a function only in two aspects:

            1. It belongs to a class and it is defined within a class.
            The first parameter in the definition of a method has to be a 
            reference "self" to the instance of the class.
        
            2. A method is called without this parameter "self".

5. What is an instance in object orientation?
    Instance is an object created from the class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   
        A class attribute is a piece of data on the class itself. When you ask 
        for it on an instance, it finds it on the class.
        An instance attribute is set directly on the object.  


"""


class Student(object):
    """ class that creates a student object with first name,
         last name and address """    
  
    def __init__(self, firstname, lastname, address):
        self.first_name = firstname
        self.last_name = lastname
        self.address = address
    

class Question(object):
    
    def __init__(self, question, answer):
        self.question = question
        self.correct_answer = answer
        
    def ask_and_evaluate(self):
        answer = raw_input(self.question) 
        return answer == self.correct_answer


class Exam(object):

    def __init__(self, name):
        self.questions = []
        self.name = name

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))                                     

    def administer(self):
        self.score = 0
        self.number_of_questions = 0
        for question in self.questions:

            if question.ask_and_evaluate() is True:
                self.score += 1
            self.number_of_questions += 1

        return self.score


def take_test(exam, student):
    student.score = exam.administer()
    return student.score


class Quiz(Exam):
    """docstring for Quiz"""
    def __init__(self, name):
        super(Quiz, self).__init__(name)

    def administer(self):

        super(Quiz, self).administer()
        if self.score <= self.number_of_questions/2:
            return "False"
        else:
            return "True"


def example(name):
    
    #exam = Exam("Madhuri")

    # exam.add_question("Which function of dictionary gets all the keys from the dictionary?", "keys()")
    # exam.add_question("nums = set([1,1,2,3,3,3,4]). What is len(nums)?", "4")
    # exam.add_question("What is the output of print list[2:] if list = [ 'abcd', 786 , 2.23 ]?", "2.23")
    # exam.add_question("Which function convert a String to a list in python?", "list()")
    # exam.add_question("Which function checks in a string that all characters are in uppercase?", "isupper()")
    # exam.add_question("Which function compares elements of both lists?", "cmp()")
    #student = Student("Joe", "Martin", "SF")
    #score = take_test(exam, student)

    quiz = Quiz("Madhuri")
    
    quiz.add_question("Which function of dictionary gets all the keys from the dictionary?", "keys()")
    quiz.add_question("nums = set([1,1,2,3,3,3,4]). What is len(nums)?", "4")
    quiz.add_question("What is the output of print list[2:] if list = [ 'abcd', 786 , 2.23 ]?", "2.23")
    quiz.add_question("Which function convert a String to a list in python?", "list()")
    quiz.add_question("Which function checks in a string that all characters are in uppercase?", "isupper()")
    quiz.add_question("Which function compares elements of both lists?", "cmp()")    

    student = Student("Ankita", "Sharma", "SF")
    score = take_test(quiz, student)

    return score


        

print example("Madhuri")







