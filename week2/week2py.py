print("--Task1--")

def find_and_print(messages):
# write down your judgment rules in comments
# your code here, based on your own rules
    for key, value in messages.items():
        if "18 years old" in value:
            print(key)
        if "college student" in value:
            print(key)
        if "legal age" in value:
            print(key)
        if "I will vote" in value:
            print(key)

find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})


print("--Task2--")

def calculate_sum_of_bonus(data):
# write down your bonus rules in comments
# your code here, based on your own rules
    total_bonus = 0
    for item in data["employees"]:
        bonus = 0
        salary = item["salary"]
        if isinstance(salary, int):
            salary = str(salary)
        if "USD" in salary:
            salary = float(salary.replace("USD", "")) * 30
        if isinstance(salary, float):
            salary = str(salary)
        if "," in salary:
            salary = salary.replace(",", "")
        if item["performance"] == "above average":
            bonus = float(salary) * 0.09
        elif item["performance"] == "average":
            bonus = float(salary) * 0.07
        else :
            bonus = float(salary) * 0.03
        if item["role"] == "Engineer":
            bonus *= 0.8
        elif item["role"] == "CEO":
            bonus *= 0.9
        else:
            bonus *= 0.7
        total_bonus += bonus
    print("Total Bonus:", '%d' %total_bonus, "TWD")

calculate_sum_of_bonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}) # call calculate_sum_of_bonus function


print("--Task3--")


def func(*data):
# your code here
    name = "沒有"
    for i in range(len(data)):
        flag = True
        for j in range(len(data)):
            if i != j:
                if data[i][1] == data[j][1]:
                    flag = False
                    break
        if flag:
            name = data[i]
            break
    print(name)
func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花 花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有


print("--Task4--")

def get_number(index):
# your code here
    lst =[0]
    last = 0
    for i in range(index):
        last +=3
        lst.append(last + 1)
        lst.append(last)

    return print(lst[index])
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

