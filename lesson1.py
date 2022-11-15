# полиморфизм
# from random import randint
#
#
# class Triangle:
#     def __init__(self, count=2):
#         self.names_values = {f"side_{i}": randint(1, 20) for i in range(count)}
#         self.square = 0
#
#     def get_attrs(self):
#         print(self.__dict__)
#
#     def get_list_attrs(self):
#         lists = list(self.__dict__.items())
#         print(lists)
#
#     def distract_square(self):
#         square = 1 / 2 * self.names_values["side_0"] * self.names_values["side_1"]
#         self.square = square
#         print(self.square)
#
# class Regtanle:
#     def __init__(self, a: int, b: int) -> None:
#         self.side_a = a
#         self.side_b = b
#         self.square = 0
#
#     def get_attrs(self) -> dict:
#         print(self.__dict__)
#
#     def get_list_attrs(self):
#         lists = list(self.__dict__.items())
#         print(lists)
#
#     def distract_square(self) -> None:
#         self.square = self.side_a * self.side_b
#         print(self.square)
#
#
# triangle1 = Triangle()
# triangle2 = Triangle()
# regtangle1 = Regtanle(12, 6)
# regtangle2 = Regtanle(16, 4)
#
#
# lists = [triangle2, regtangle1 , triangle1, regtangle2]
# for i in lists:
#     i.distract_square()
#     i.get_attrs()
#     i.get_list_attrs()

# ####

# full_name: str
# course: int = 1
# subjects : dict = {}
# total = 0


# class Student:
#     def __init__(self, full_name, course):
#         self.full_name = full_name
#         self.course = course
#         self.subjects = {}
#         self.total = 0
#
#     def set_subjects(self, subjects: dict) -> None:
#             self.subjects = subjects
#
#     def get_total(self):
#             self.total = sum(self.subjects.values()) / len(self.subjects)
#
#     def save_total_in_file(self):
#             with open(f"{self.full_name}.txt", "a") as f:
#                 f.write(f"{self.full_name} - {self.course} - {self.total}\n")
#                 for key, value in self.subjects.items():
#                     f.write(f"{key} - {value}\n")
#             self.total = 0
#             self.subject = {}
# subjects = {
#         "algebra": 70,
#         "python": 56,
# }
#
# subjects2 = {
#         "algebra": 70,
#         "python": 56,
#         "java": 80
# }
# sman = Student("sman sagun", 2)
# sman.set_subjects(subjects)
# sman.get_total()
# sman.save_total_in_file()
# sman.set_course()
# sman.set_subjects(subjects2)
# sman.get_total()
# sman.save_total_in_file()
#


