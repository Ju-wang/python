for week in range(1, 51):
    with open(str(week)+"주차.txt", "w", encoding="utf8") as report:
        report.write("-"+str(week)+"주차 주간보고- \n부서: \n이름: \n업무 요약:")
