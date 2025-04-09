##################
#프로그래명: 성적관리프로그램(객체지향 프로그램)
#작성자: 소프트웨어학과/서윤제
#작성일: 2025/04/09
#프로그램 설명: 학생의 세개의 교과목(영어, C-언어, 파이썬)에 대하여 키보드로부터 입력할 시 성적 계산 관련 Class를 제공해준다.
##################

import numpy as np
import pandas as pd


class Object_Oriented_Programming:

    def __init__(self, total_student = 5):
        self.total_student = total_student                                

    def __info_input(self,):
        """입력 함수"""

        student_info = {}

        student_number = int(input("학번: ")); student_info["학번"] = student_number
        student_name = input("이름: "); student_info["이름"] = student_name
        student_english = int(input("영어: ")); student_info["영어"] = student_english
        student_c_lang = int(input("C-언어: ")); student_info["C-언어"] = student_c_lang
        student_python = int(input("파이썬: ")); student_info["파이썬"] = student_python

        return student_info

    def __score_calc(self, student_info):
       """총점, 평균 구하기 함수"""

       ## 총점 구하기

       sum = student_info["영어"] + student_info["C-언어"] + student_info["파이썬"]
       student_info['총점'] = sum

       ## 평균 구하기
       avg = np.round(sum / 3, 1)
       student_info['평균'] = avg

       return student_info

    def __grade_calc(self, student_info):
        """학점 구하기 함수"""

        student_info['학점'] = student_info['평균']
        return student_info


    def __rank_calc(self, students_info):
        """등수 구하기 함수"""
        score = []

        for info in students_info:
            score.append(info['총점'])
    
        sorted_score = sorted(score, reverse=True)
        ranks = [sorted_score.index(x) + 1 for x in score]

        for i, rank in enumerate(ranks):
            students_info[i]["등수"] = rank
 

        return students_info


    def __print_info(self, total_student):
        """출력 함수"""

        students_info = []

        for i in range(total_student):
            student_info = self.__info_input() ## 학번, 이름, 교과목 점수 입력받기
            student_info = self.__score_calc(student_info) ## 평균, 총점 구하기
            student_info = self.__grade_calc(student_info) ## 학점 구하기
            students_info.append(student_info)

        students_info = self.rank_calc(students_info) ## 등수 구하기

        print("#"*25)
        print("###성적관리 프로그램")
        print("#"*25)

        print("="*50); print("\n")

        print("학번                    이름              영어      C-언어      파이썬         총점       평균         학점          등수")

        print("="*50)

        for student_info in students_info:
            print(f'{student_info["학번"]}                    {student_info["이름"]}                {student_info["영어"]}      {student_info["C-언어"]}      {student_info["파이썬"]}         {student_info["총점"]}       {student_info["평균"]}         {student_info["학점"]}         {student_info["등수"]}')

        return students_info

    def __insert(self, students_info):
        return None


    def __delete(self, students_info, student_name):
        for i, info in enumerate(students_info):
            if info['이름'] == student_name:
                students_info.pop(i)
                break

        return students_info

    def __searching(self, students_info, student_name, student_number):
        for info in students_info:
            if info['이름'] == student_name & info['학번'] == student_number:
                return info

            return None

    def __sorting(self, students_info):
        scores = []

        for info in students_info:
            scores.append[info['총점']]

        return scores.sort(reverse=True)

    def __80_score(self,students_info):

        count = 0

        for info in students_info:
            if info['총점'] >= 80:
               count++

        return count           
