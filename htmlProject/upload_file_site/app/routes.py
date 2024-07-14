from flask import render_template, request, redirect, url_for
from app import app

# 사람들의 정보를 딕셔너리로 저장
people = [
    {'이름': '김상순', '전화번호': '010-1234-5678', '취미': ['컴퓨터 게임', '등산'], '자기소개': '친구를 찾고 있어요!'},
    {'이름': '김상익', '전화번호': '010-9876-5432', '취미': ['요리', '그림 그리기'], '자기소개': '컴퓨터 공학과 4학년 김상익입니다.'},
    {'이름': '도영익', '전화번호': '010-5555-6666', '취미': ['요리', '독서'], '자기소개': '오징어 심리학과에 다니는 도영익입니다.'},
    {'이름': '이온상', '전화번호': '010-3333-4444', '취미': ['여행', '사진 촬영'], '자기소개': '안녕하세요! 삼육대 두유공학과에 다니고 있습니다.'},
]

@app.route('/') #검색 페이지, 사람목록 확인 메인 페이지
def index():
    return render_template('index.html', people=people)

@app.route('/person/<int:id>') #사람들 정보 상세 페이지, 딕셔너리 값이 저장된 배열의 순서를 값으로 가짐
def person(id):
    person = people[id]
    return render_template('person.html', person=person)

@app.route('/search', methods=['GET', 'POST']) # 사람들 목록을 그 사람이 가진 취미로 검색하고 출력함
def search():
    if request.method == 'POST':
        hobby = request.form.get('hobby')
        matched_people = [person for person in people if hobby in person['취미']]
        return render_template('index.html', people=matched_people, search_query=hobby)
    return render_template('index.html', people=people)
