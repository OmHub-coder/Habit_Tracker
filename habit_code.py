import datetime
class Habit:

    def add_habit(self,hab):
        with open("habit_record.txt","a") as f:
            if len(hab)!=0:
                f.write(hab+":\n")
            else:
                return "enter valid habit"
        return "Habit is added."



    @staticmethod
    def mark_habit():

        try:
            with open ("habit_record.txt","r") as f:
                data=f.readlines()
        except FileNotFoundError:
            return "add habit in file first"

        if len(data)==0:
            return "No habit stored"

        for number,line in enumerate(data,start=1):
            print(number,line.strip())

        while True:
            today=(datetime.date.today().isoformat())

            try:
                choice=int(input("Enter the no. of habit you want to mark :  "))
            except Exception as e:
                print("please enter valid number")
                continue

            if choice<1 or choice>len(data):
                print("No. habit with that number.")
                continue
            if data[choice-1][:-1].endswith(":"):
                data[choice-1]=(data[choice-1]).rstrip("\n")+today+"\n"
            else:

                if today not in data[choice-1] :
                    data[choice-1]=(data[choice-1]).rstrip("\n")+","+today+"\n"
                else:
                    print("You already marked this habit today.")

            conti=input("Enter whether you want to continue or not (y/n) : ")
            if conti =="y":
                continue
            else :
                break

        with open("habit_record.txt","w") as f:
            f.writelines(data)
        return "Your records was marked."


    
    @staticmethod
    def Veiw_today():
        today=(datetime.date.today().isoformat())
        
        try:
            with open("habit_record.txt","r") as f:
                data=f.readlines()
        except FileNotFoundError:
            return "no habit in file add it first."
        
        if len(data)==0:
            return "No habit stored yet."
        
        print("\n\nhabit marked done are : \n")
        for i in data:
            if today in i :
                print(i.strip().split(":")[0])

        
        print("\n\nhabit that are pending to be marked done : \n")
        for i in data:
            if today not in i :
                print(i.strip().split(":")[0])

        return "This is your progress."



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

        elif choice == 2:
            obj.mark_habit()

        elif choice==3:
            obj.Veiw_today()
        else:
            break