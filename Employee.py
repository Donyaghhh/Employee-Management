Employee_Info={
    39925:{"name":"Arman","last_name":"Ghorbani","employee_post":"programmer","work_year":5,"Salary":60000000},
    40020:{"name":"Farhad","last_name":"Ghaderi","employee_post":"IT_managment","work_year":10,"Salary":100000000},
    40128:{"name":"Zahra","last_name":"Sarmadi","employee_post":"project_manager","work_year":20,"Salary":150000000}
}

#print list employee
#----------section 1-------------------------
employee=[]
for key,value in Employee_Info.items():
        #p=(value["name"],value["last_name"])
        name=value["name"]
        last_name=value["last_name"]
        p=(f"{name},{last_name}:{value}")
        employee.append(p)
print(employee)


print(30 * "*")
#print information special employee
#-------------section 2--------------------------
employee_id=int(input("enter number that you want"))
if employee_id in Employee_Info:
        print(Employee_Info[employee_id])
else:
        print("not found")

print(30 * "-")
#print work year up 10 
#-----------section 3-----------------------
for key,value in Employee_Info.items():
        if value["work_year"]>10:
                print("employee_id=",[key],value["name"],value["last_name"])
