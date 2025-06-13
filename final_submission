##################
#프로그래명: 성적관리프로그램
#작성자: 소프트웨어학과/서윤제
#작성일: 2025/06/13
#프로그램 설명: 학생의 세개의 교과목(영어, C-언어, 파이썬)에 대하여 키보드로부터 입력할 시 성적 계산 관련 Class를 제공해준다.
##################

class Student:
    def __init__(self, student_id, name, eng, c_lang, python):
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.c_lang = c_lang
        self.python = python
        self.total = 0
        self.avg = 0.0
        self.grade = ''
        self.rank = 0
        self.calculate_total_avg()
        self.calculate_grade()

    def calculate_total_avg(self):
        self.total = self.eng + self.c_lang + self.python
        self.avg = self.total / 3

    def calculate_grade(self):
        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:
            self.grade = 'B'
        elif self.avg >= 70:
            self.grade = 'C'
        elif self.avg >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'


def input_students():
    students = []
    n = int(input("학생 수를 입력하세요: "))
    for _ in range(n):
        student_id = input("학번: ")
        name = input("이름: ")
        eng = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))
        students.append(Student(student_id, name, eng, c_lang, python))
    return students


def calculate_ranks(students):
    for s in students:
        s.rank = 1
        for other in students:
            if other.total > s.total:
                s.rank += 1


def print_students(students):
    print("\n{:<10}{:<10}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}".format(
        "학번", "이름", "영어", "C", "파이썬", "총점", "평균", "학점", "등수"
    ))
    for s in students:
        print("{:<10}{:<10}{:<6}{:<6}{:<6}{:<6}{:<6.2f}{:<6}{:<6}".format(
            s.student_id, s.name, s.eng, s.c_lang, s.python,
            s.total, s.avg, s.grade, s.rank
        ))


def insert_student(students):
    student_id = input("학번: ")
    name = input("이름: ")
    eng = int(input("영어 점수: "))
    c_lang = int(input("C-언어 점수: "))
    python = int(input("파이썬 점수: "))
    student = Student(student_id, name, eng, c_lang, python)
    students.append(student)
    calculate_ranks(students)
    print("학생이 추가되었습니다.")


def delete_student(students):
    student_id = input("삭제할 학생의 학번을 입력하세요: ")
    for s in students:
        if s.student_id == student_id:
            students.remove(s)
            calculate_ranks(students)
            print("삭제되었습니다.")
            return
    print("해당 학번을 찾을 수 없습니다.")


def search_student(students):
    keyword = input("학번 또는 이름을 입력하세요: ")
    for s in students:
        if s.student_id == keyword or s.name == keyword:
            print("\n검색 결과:")
            print("{:<10}{:<10}{:<6}{:<6}{:<6}{:<6}{:<6.2f}{:<6}{:<6}".format(
                s.student_id, s.name, s.eng, s.c_lang, s.python,
                s.total, s.avg, s.grade, s.rank
            ))
            return
    print("검색 결과가 없습니다.")


def sort_students_by_total(students):
    students.sort(key=lambda s: s.total, reverse=True)
    calculate_ranks(students)
    print("총점 기준으로 정렬되었습니다.")


def count_above_80(students):
    count = sum(1 for s in students if s.avg >= 80)
    print(f"\n평균이 80점 이상인 학생 수: {count}")


def main():
    students = input_students()
    calculate_ranks(students)

    while True:
        print("\n메뉴:")
        print("1. 전체 출력")
        print("2. 학생 추가")
        print("3. 학생 삭제")
        print("4. 학생 검색")
        print("5. 총점으로 정렬")
        print("6. 평균 80점 이상 학생 수")
        print("0. 종료")

        choice = input("선택: ")

        if choice == '1':
            print_students(students)
        elif choice == '2':
            insert_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            sort_students_by_total(students)
        elif choice == '6':
            count_above_80(students)
        elif choice == '0':
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()
