from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["번호", "게임 정보"]
table.add_row([1, "리그오브레전드"])
table.add_row([2, "FC온라인"])
table.add_row([3, "배틀그라운드"])
table.add_row([4, "발로란트"])
table.add_row([5, "서든어택"])
table.add_row([6, "메이플 스토리"])
table.add_row([7, "오버워치"])
table.add_row([8, "스타크래프트"])
table.add_row([9, "던전앤파이터"])
table.add_row([10, "로스트아크"])

table.add_column("점유율",["37.17%","10.61%","10.16%","8%","6.25%","5.09%","4.07%","2.3%","1.63%","1.55%"])

print(table)