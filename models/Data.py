from User import User
from Quiz import Quiz
from Subjects import Subjects

list_of_users = [
    User("Emna Kallel","emna"),
    User("achraf", "achraf"),
    User("emna","emna", True),
    User("Roukaya Kallel", "roukaya", True), 
]

list_of_questions = [
    Quiz("I Love Toutou", True, 3),
    Quiz("I Dont' Love Toutou", False, 1),
    Quiz("Toutou Assoul", True, 2),
]

list_of_subjects = [
    Subjects("Hematology", None, None),
    Subjects("Microbiology", None, None),
    Subjects("Parasitology", None, None),
    Subjects("Virology", None, None),
    Subjects("Biochemestry", None, None),
    Subjects("Immunology", None, None),
    Subjects("Pharmacology", None, None),
    Subjects("Analytical Chemistry", None, None),
    Subjects("Therapeutic Chemistry", None, None),
    Subjects("Physical Chemistry", None, None),
]