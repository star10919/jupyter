#%%
# 1. 판다스와 넘파이를 임포트하시오
import pandas as pd
import numpy as np
from icecream import ic


if __name__ == '__main__':

    menu = input('')
'''
 '0. 종료\n'
 '2. 판다스 버전 출력\n'
 '3. 판다스 라이브러리 버전 정보 모두 출력하기\n'
 '4. 주어진 값으로 DataFrame 객체를 생성하시오.\n'
 '5. 객체내부 정보를 출력하기\n'
 '6. 객체 상위 3열까지 출력하기\n'
 '7. animal과 age 컬럼만 출력하기\n'
 '8. 객체의 3, 4, 8번 행에 해당하는 animal과 age값만 출력하기\n'
 '9. visits 컬럼에서 2 초과하는 값 출력\n'
 '10. age 에서 NaN 값 출력\n'
 '11. age가 3살 미만 고양이값 출력\n'
 '12. age가 2살이상 4살 미만인 값 출력\n'
 '13. f 행의 나이를 1.5살로 변경\n'
 '14. 객체에서 visits 의 합 출력\n'
 '15. 동물별로 나이의 평균 출력\n'
 '16-1. k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가\n'
 '16-2. 방금 추가한 열 삭제\n'
 '17. 객체에 있는 동물의 종류의 수 출력\n'
 '18. age 는 내림차순, age가 같은 경우 visits 는 오름차순으로 정렬\n'
 '19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력\n'
 '20. snake 를 python 으로 값을 변경\n'
 '21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.\n')
'''

    def quiz_2():
        # 2. 판다스 버전 체크하기
        ic(pd.__version__)

    def quiz_3():
    # 3. 판다스 라이브러리 버전 정보 모두 출력하기
        pd.show_versions()

    def quiz_4():
    # 4. 주어진 값으로 DataFrame 객체를 생성하시오.
        data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        df = pd.DataFrame(data, index=[labels])
        df

    def quiz_5():
        # 5. 객체내부 정보를 출력하기
        df.describe()

    def quiz_6():
        # 6. 객체 상위 3열까지 출력하기
        df.head(3)
        # df.iloc[:(3)]

    def quiz_7():
        # 7. animal과 age 컬럼만 출력하기
        df[['animal', 'age']]
        # df.loc[:,['animal','age']]

    def quiz_8():
        # 8. 객체의 3, 4, 8번 행에 해당하는 animal과 age값만 출력하기
        df.loc[['c', 'd', 'h'], ['animal', 'age']]
        # df.loc[df.index[[2,3,7]],['animal','age']]

    def quiz_9():
        # 9. visits 컬럼에서 2 초과하는 값 출력
        df[df['visits'] > 2]

    def quiz_10():
        # 10. age 에서 NaN 값 출력
        ag = df.isnull()
        age = df[ag['age'] == True]
        age
        # df[df['age'].isnull()]

    def quiz_11():
        # 11. age가 3살 미만 고양이값 출력
        df[(df['age'] < 3) & (df['animal'] == 'cat')]

    def quiz_12():
        # 12. age가 2살이상 4살 미만인 값 출력
        df[(df['age'] >= 2) & (df['age'] < 4)]
        # df[df['age'].between(2,4)]

    def quiz_13():
        # 13. f 행의 나이를 1.5살로 변경
        df.at['f', 'age'] = 1.5
        df
        # df.loc['f','age'] = 1.5

    def quiz_14():
        # 14. 객체에서 visits 의 합 출력
        df['visits'].sum()

    def quiz_15():
        # 15. 동물별로 나이의 평균 출력
        df.groupby('animal')['age'].mean()

    def quiz_16_1():
        # 16. k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가
        df.loc['k'] = ['dog', 5.5, 2, 'no']  # column 순서대로 넣기
        df

    def quiz_16_2():
        # 16. 방금 추가한 열 삭제
        df.drop('k', inplace=True)  # 할당하지 말기
        # del df['k']
        df

    def quiz_17():
        # 17. 객체에 있는 동물의 종류의 수 출력
        df['animal'].value_counts()

    def quiz_18():
        # 18. age 는 내림차순, age가 같은 경우 visits 는 오름차순으로 정렬
        df.sort_values(by=['age', 'visits'], ascending=[False, True])  # False:내림차순, True:오름차순

    def quiz_19():
        # 19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력
        df['priority'] = df['priority'].map({"yes": True, "no": False})
        df

    def quiz_20():
        # 20. snake 를 python 으로 값을 변경
        df['animal'] = df['animal'].replace('snake', 'python')
        df

    def quiz_21():
        # 21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.
        # 즉,각 행은 animal 이고, 각 열은 visits 이며, 값은 평균연령
        # (힌트, 피벗 테이블을 활용해야 함)   Aggregation function : 집계합수(sum,max,count,min)
        df = df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')
        df

    while 1:
        if menu == '0':
            break
        elif menu == '2':
            quiz_2()
        elif menu == '3':
            quiz_3()
        elif menu == '4':
            quiz_4()
        elif menu == '5':
            quiz_5()
        elif menu == '6':
            quiz_6()
        elif menu == '7':
            quiz_7()
        elif menu == '8':
            quiz_8()
        elif menu == '9':
            quiz_9()
        elif menu == '10':
            quiz_10()
        elif menu == '11':
            quiz_11()
        elif menu == '12':
            quiz_12()
        elif menu == '13':
            quiz_13()
        elif menu == '14':
            quiz_14()
        elif menu == '15':
            quiz_15()
        elif menu == '16_1':
            quiz_16_1()
        elif menu == '16_2':
            quiz_16_2()
        elif menu == '17':
            quiz_17()
        elif menu == '18':
            quiz_18()
        elif menu == '19':
            quiz_19()
        elif menu == '20':
            quiz_20()
        elif menu == '21':
            quiz_21()
        else:
            continue