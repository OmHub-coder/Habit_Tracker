class Habit:

    def add_habit(self,hab):
        with open("habit_record.txt","a") as f:
            if len(hab)!=0:
                f.write(hab+":\n")
            else:
                return "enter valid habit"
        return "Habit is added."


# ___________main___________
if __name__=="__main__":
    obj=Habit()
    print("\n______________Welcome to the habit tracker application______________\n")
    while True:
        print("\n1.Add a habit\n2.Mark the habit as done\n3.Veiw your habit mark done today\n4.exit\n")

        try:
            choice=int(input("Enter your choice : "))
        except Exception as e :
            print("Invalid choice",e)
            continue

        if choice == 1 :
            hab=input("Enter the habit to be added : ")
            print(obj.add_habit(hab))
        else:
            break