import pandas as pd
import numpy as np

# 데이터 칼럼, 칼럼 명
# 1 이름<batter_name> 2 나이<age> 3 출장 경기 수<G> 4 타수<PA> 5 타석 수<AB>
# 6 득점<R> 7 안타<H> 8 2루타<2B> 9 3루타<3B> 10 홈런<HR>
# 11 총 루타 수<TB> 12 타점<RBI> 13 도루 성공<SB> 14 도루 실패 15<CS> 볼넷<BB>
# 16 시구<HBP> 17 고의 4구<GB> 18 삼진<SO> 19 병살타<GDP> 20 희생타<BU>
# 21 희생 플라이<fly> 22 해당 시즌<year> 23 해당 시즌의 연봉<salary>
# 24 승리 기여도<war> 25 선수 태어난 연도<year_born>
# 26 타석 위치<hand2> 27 최근 포지션<cp> 28 통합 포지션<tp> 29 1루타<1B> 30 FBP(볼넷 + 시구)<FBP>
# 31 avg 타율<avg> 32 출루율<OBP> 33 장타율<SLG> 34 OPS(출루율 + 장타율)<OPS> 35 다음 시즌<p_year>
# 36 다음 시즌 타석 수<YAB> 37 다음 시즌 ops<YOPS>

# 데이터 생성
# 데이터 shape (1913, 37)
csv_data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
df = pd.DataFrame(csv_data)


# 2-1-1
def num_1():
    # 문제 풀이에 필요한 칼럼 = 이름1<batter_name>, 안타7<H>, 타율31<avg>
    # 홈런10<HR>, 출루율32<OBP>, 해당 시즌22<year>
    col = ['H', 'HR', 'avg', 'OBP']
    col_2 = ['안타', '홈런', '타율', '출루율']

    for i in range(2015, 2019):
        for j in range(4):
            # 2015 ~ 2019 시즌별 행 추출
            print('-' * 20)
            print(f"{i} 시즌 {col_2[j]} top 10 선수")
            print(' '.join(df.loc[(df.year == i), ].sort_values(by=[col[j]], ascending=False)
                  .iloc[0:10, 0].values))
            print('-' * 20)


# 2-1-2
def num_2():
    col = ['war']
    col_2 = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
    for j in range(8):
        print('-' * 20)
        print(f"{2018} 시즌 top {col_2[j]}")
        print(df.loc[(df.year == 2018) & (df.cp == col_2[j]), ]
                       .sort_values(by=[col[0]], ascending=False).iloc[0, 0])
        print('-' * 20)


# 2-1-3
def num_3():
    # 문제 풀이에 필요한 칼럼
    # 5<R>, 6<H>, 9<HR>, 11<RBI>, 12<SB>,  22<salary>, 23<war>, 30<avg>, 31<OBP>, 32<SLG>
    col = ['득점(R)', '안타(H)', '홈런(HR)', '타점(RBI)',
           '도루(SB)', '승리 기여도(war)', '타율(avg)', '출루율(OBP)', '장타율(SLG)']
    corr_data = pd.DataFrame(df.iloc[:, [5, 6, 9, 11, 12, 22, 23, 30, 31, 32]])
    corr_data = pd.DataFrame(corr_data.corr())
    # 상관 계수가 클수록 두 변수 사이의 관계가 직선적 이다.
    corr_list = list(corr_data.iloc[5, ].values)
    # 상관 계수가 1.0000 인것은 salary와 salary의 관계이다.
    for i in range(len(corr_list)):
        if int(corr_list[i]) == 1:
            corr_list.pop(i)
            break
    # 1을 제외한 가장 큰 상관 계수 구하기
    max_corr = max(corr_list)
    for i in range(len(corr_list)):
        if corr_list[i] == max_corr:
            print(f"\n연봉과 가장 상관 계수가 높은 것은 {col[i]}입니다")


print('oss 과제 2 - 1')
print('이름 : 고성민')
print('학번 : 12221828')
print('\n숫자별 메뉴\n')
print('1 => 과제 2 - 1 - 1)')
print('2 => 과제 2 - 1 - 2)')
print('3 => 과제 2 - 1 - 3)')
print('4 => 프로그램 종료')

while True:
    try:
        print('\n숫자를 입력하세요. (1 ~ 4)')
        num = int(input().rstrip())
        if 1 <= num <= 4:
            if num == 1:
                num_1()
            elif num == 2:
                num_2()
            elif num == 3:
                num_3()
            else:
                print('\n프로그램을 종료합니다')
                break
        else:
            print('올바른 숫자를 입력하세요')
            continue
    except:
        print('올바른 숫자를 입력하세요')