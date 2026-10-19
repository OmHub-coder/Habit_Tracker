import datetime # date module to get date

#class creation
class Habit:
    
    # function to read the file in line format andd return data in list
    def read(self):
        try:
            with open("habit_record.txt","r") as f:
                data=f.readlines()
                return data
        except FileNotFoundError:
            return []



    #function to add habit in file
    def add_habit(self, hab):
        hab = hab.strip()

        if not hab:
            return "Enter a valid habit."

        with open("habit_record.txt", "a") as f:
            f.write(hab + ":\n")

        return "Habit is added."



    #function to mark habit as done in file
    def mark_habit(self):

        data=obj.read()     #to read data from file using read function

        if len(data)==0:
            return "No habit stored"
        
        today=(datetime.date.today().isoformat())   #to get today date in YYYY-MM-DD format

        while True:
            for number,line in enumerate(data,start=1):       
                print(number,line.strip())

            try:
                choice=int(input("Enter the no. of habit you want to mark :  "))
            except ValueError:
                print("please enter valid number")
                continue

            if choice<1 or choice>len(data):
                print("No. habit with that number.")
                continue

            left, right = data[choice-1].strip().split(":")
            if right == "":
             # first mark
                data[choice-1]=(data[choice-1]).rstrip("\n")+today+"\n"             

            else:

                dates = right.split(",") if right else []
                if today not in dates:
                    data[choice-1] = (data[choice-1].rstrip("\n") + "," + today + "\n")
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


    
    #function to view whether the habit is done or not today
    def veiw_today(self):
        today=(datetime.date.today().isoformat())
        
        data=obj.read()

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



    #function t delete a existing habit from data    
    def delete_habit(self):
        
        data=obj.read()

        if len(data)==0:
            return "NO habit in file first add the habit."


        while True:
            for number,line in enumerate(data,start=1):
                print(number,line.strip().split(":")[0])

            try:
                choice=int(input("Enter the number of habit you want to remove : "))
            except ValueError:
                print("enter the valid number.")
                continue

            if choice < 1 or choice > len(data):
                print("No habit with that number.")
                continue
            else :
                data.pop(choice-1)

            for number,line in enumerate(data,start=1):
                print(number,line.strip().split(":")[0])

            conti=input("Whether you want to continue deleting the habit or not (y/n) : ")
            if conti != "y":
                break

        with open("habit_record.txt","w") as f:
            f.writelines(data)


        return "Your habit is deleted."


    
    #function to rename a habit 
    def rename_habit(self):
        
        data=obj.read()
        
        if len(data)==0:
            return "no habit to be renamed."

        
        while True:
            for number,line in enumerate(data,start=1):
                print(number,line.strip().split(":")[0])

            try:
                choice=int(input("Enter the no. of which you want to rename :  "))
            except ValueError:
                print("enter valid input")
                continue
             
            if choice<1 or choice>len(data):
                print("Enter the valid number to select the habit.")
            else:
                rename=input("Enter the new name of habit :  ").strip()
                if not rename or ":" in rename:
                    print("Enter the valid name without : this  ")
                    continue
                else:
                    left,right=data[choice-1].strip().split(":")
                    data[choice-1]=rename+":"+right+"\n"
            
            conti=input("Enter whether you want to continue or not (y/n):  ").strip()
            if conti not in "yY":
                break

        with open("habit_record.txt","w") as f:
            f.writelines(data)
        
        return "Your habit was sucessfuly renamed."
    
            

# ___________main___________

if __name__=="__main__":

    #object creation
    obj=Habit()

    #MENU
    print("\n______________Welcome to the habit tracker application______________\n")

    #infinite loop t take choice of user
    while True:
        print("\n1.Add a habit\n2.Mark the habit as done\n3.Veiw your habit mark done today\n4.Deleting a habit\n5.Rename a habit\n6.exit\n")

        try:
            choice=int(input("Enter your choice : "))
        except Exception as e :
            print("Invalid choice",e)
            continue

        if choice == 1 :
            hab=input("Enter the habit to be added : ")
            print(obj.add_habit(hab))

        elif choice == 2:
            print(obj.mark_habit())

        elif choice==3:
            print(obj.veiw_today())

        elif choice == 4 :
            print(obj.delete_habit())
        
        elif choice ==5 :
            print(obj.rename_habit())

        elif choice==6:
            break

        else:
            print("Invalid choice")