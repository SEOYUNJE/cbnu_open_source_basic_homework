##################
#프로그래명: 성적관리프로그램
#작성자: 소프트웨어학과/서윤제
#작성일: 2025/04/02
#프로그램 설명: 학생의 세개의 교과목(영어, C-언어, 파이썬)에 대하여 키보드로부터 입력할 시 성적 관련 여러 함수를 제공해줌
##################

import numpy as np
import pandas as pd

def info_input():
    """입력 함수"""

    student_info = {}

    student_number = int(input("학번: ")); student_info["학번"] = student_number
    student_name = input("이름: "); student_info["이름"] = student_name
    student_english = int(input("영어: ")); student_info["영어"] = student_english
    student_c_lang = int(input("C-언어: ")); student_info["C-언어"] = student_c_lang
    student_python = int(input("파이썬: ")); student_info["파이썬"] = student_python

    return student_info

def score_calc(student_info):
    """총점, 평균 구하기 함수"""

    ## 총점 구하기

    sum = student_info["영어"] + student_info["C-언어"] + student_info["파이썬"]
    student_info['총점'] = sum

    ## 평균 구하기
    avg = np.round(sum / 3, 1)
    student_info['평균'] = avg

    return student_info

def grade_calc(student_info):
    """학점 구하기 함수"""

    student_info['학점'] = student_info['평균']
    return student_info


def rank_calc(students_info):
    """등수 구하기 함수"""
    score = []

    for info in students_info:
        score.append(info['총점'])
    sorted_score = sorted(score, reverse=True)
    ranks = [sorted_score.index(x) + 1 for x in score]

    for i, rank in enumerate(ranks):
        students_info[i]["등수"] = rank


    return students_info


def print_info(total_student):
    """출력 함수"""

    students_info = []

    for i in range(total_student):
        student_info = info_input() ## 학번, 이름, 교과목 점수 입력받기
        student_info = score_calc(student_info) ## 평균, 총점 구하기
        student_info = grade_calc(student_info) ## 학점 구하기
        students_info.append(student_info)

    students_info = rank_calc(students_info) ## 등수 구하기

    print("#"*25)
    print("###성적관리 프로그램")
    print("#"*25)

    print("="*50); print("\n")

    print("학번                    이름              영어      C-언어      파이썬         총점       평균         학점          등수")

    print("="*50)

    for student_info in students_info:
        print(f'{student_info["학번"]}                    {student_info["이름"]}                {student_info["영어"]}      {student_info["C-언어"]}      {student_info["파이썬"]}         {student_info["총점"]}       {student_info["평균"]}         {student_info["학점"]}         {student_info["등수"]}')

    return students_info

def insert(students_info):
    return None


def delete(students_info, student_name):
    for i, info in enumerate(students_info):
        if info['이름'] == student_name:
           students_info.pop(i)
           break

    return students_info

def searching(students_info, student_name, student_number):
    for info in students_info:
        if info['이름'] == student_name & info['학번'] == student_number:
            return info

    return None

def sorting(students_info):
    scores = []

    for info in students_info:
        scores.append[info['총점']]

    return scores.sort(reverse=True)

def 80_score(students_info):

    count = 0

    for info in students_info:
        if info['총점'] >= 80:
           count++

    return count

board= [[' ' for x in range (3)] for y in range(3)]

while True:
  for r in range(3):
     print(" " + board[r][0 + "| " + board[r][1] + "| " + board[r][2]])

     if (r!=2):
         print("---|---|---")

  x = int(input("다음 수의 x좌표를 입력하시오"))
  y = int(input("다음 수의 y좌표를 입력하시오"))
