


week_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
tasks = ["java", "sleep", "python", "data science", "catch cruise", "flex", "flex"]

zip(week_days, tasks)

def to_do_list(days_of_week):
    to_do_list = {}
    for x,y in zip(week_days, tasks):
        to_do_list[x] = y
    return to_do_list
def main():
    to_do_list(tasks)
    print(to_do_list(tasks))
main()



