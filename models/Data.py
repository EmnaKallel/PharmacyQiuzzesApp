from User import User
from Quiz import Quiz, QuestionOption
from Subject import Subject
from Test import Test


list_of_users = [
    User("Emna Kallel","emna"),
    User("achraf", "achraf"),
    User("emna","emna", True),
    User("Roukaya Kallel", "roukaya", True), 
]

list_of_subjects = [
    Subject("Hematology", [ 
        Test("Test 1 = ImmunoHematology",[
            Quiz("what are the requirements for blood <Br> grouping?", [
                QuestionOption("A: Use the same test serum by two different technicians"),
                QuestionOption("B: Use two different test sera by the same technician"),
                QuestionOption("C: Including a Beth-Vincent globular test and a Simonin seric test", True),
                QuestionOption("D: Use two different test sera by two different technicians", True),
            ]),
            Quiz("which blood types can be a donor for <Br> group O+?", [
                QuestionOption("A: O-", True),
                QuestionOption("B: A+"),
                QuestionOption("C: B+"),
                QuestionOption("D: AB+"),
            ]),
            Quiz("Which blood types can be a donor for <Br> group A-?", [
                QuestionOption("A: O-", True),
                QuestionOption("B: AB-"),
                QuestionOption("C: A-"),
                QuestionOption("D: O+"),
            ]),
        ]),
        Test("Test 2 = Hemostasis",[
            Quiz("What are the etiologies of isolated Prothombin Time prolongation?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
            Quiz("what are the etiologies of an isolated activated partial thromboplastin time prolongation?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
            Quiz("what are the etiologies for prolonged activated cephalin time and prothombin time?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
        ]),
        Test("Test 3 = HematoCytology",[
            Quiz("what red blood cell abnormalities can be found in a Pap smear?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
            Quiz("what reagents should be used when staining a smear?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
            Quiz("what is the upper and lower limit of platelets for a Pap smear?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
        ]),
        Test("Test 4 = Anemia",[
            Quiz("what is the lower limit of hemoglobin for children?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
            Quiz("what are the etiologies of microcytic anemia?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
            Quiz("what are the etiologies of macrocytic or normocytic anemia?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
        ]),
        Test("Test 5 = Leukemias",[
            Quiz("what is the upper lymphocyte limit?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
            Quiz("what are the arguments for acute myeloid leukemia?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
            Quiz("what are the arguments for chronic lymphocytic leukemia?", [
                QuestionOption("A: "),
                QuestionOption("B: "),
                QuestionOption("C: "),
                QuestionOption("D: "),
            ]),
        ]),
    ],),
    
    Subject("Microbiology"),
    Subject("Parasitology"),
    Subject("Virology"),
    Subject("Biochemestry"),
    Subject("Immunology"),
    Subject("Pharmacology"),
    Subject("Analytical Chemistry"),
    Subject("Therapeutic Chemistry"),
    Subject("Physical Chemistry"),
]