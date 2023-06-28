class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        self.next = None

class HashTable:
    def __init__(self, size):
        self.table = [None] * size

    def hash(self, key):
        return key % len(self.table)

    def get(self, key):
        index = self.hash(key)
        student = self.table[index]
        while student is not None:
            if student.student_id == key:
                return student
            student = student.next
        return None

    def set(self, name, student_id, gpa):
        student = self.get(student_id)
        if student is not None:
            student.name = name
            student.gpa = gpa
        else:
            index = self.hash(student_id)
            new_student = Student(name, student_id, gpa)
            new_student.next = self.table[index]
            self.table[index] = new_student

    def remove(self, key):
        index = self.hash(key)
        student = self.table[index]
        prev_student = None
        while student is not None:
            if student.student_id == key:
                if prev_student is None:
                    self.table[index] = student.next
                else:
                    prev_student.next = student.next
                return
            prev_student = student
            student = student.next

    def __str__(self):
        result = ""
        for student in self.table:
            while student is not None:
                result += f"Name: {student.name}, Student ID: {student.student_id}, GPA: {student.gpa}\n"
                student = student.next
        return result


def main():
    
    hash_table = HashTable(10)
    hash_table.set("Alice", 555, 8.5)
    hash_table.set("Bob", 456, 7.8)
    hash_table.set("Charlie", 789, 9.2)

    print(hash_table.get(555))
    print(hash_table.get(456).name)  
    
    hash_table.remove(555)
    print(hash_table.get(555))  
    print(hash_table)


if __name__== "__main__":
    main()