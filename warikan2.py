def warikan(amount, number_of_people):
    return f"一人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円"


# Table1: 1500円で3人
print(warikan(amount=1500, number_of_people=3))
# Table2: 2000円で3人
print(warikan(amount=2000, number_of_people=3))
# Table3: 3647円で4人
print(warikan(amount=3647, number_of_people=4))
# Table5: 5000円で6人
print(warikan(amount=5000, number_of_people=6))
