name= "Tarun"

t = {'roll':"21AK45",'Year':"3rd Year",'branch':"CSE"}
marks = [15,89,56,12]

def printinfo():
    print(f":::::{name} Details:::::")
    print(f"Roll Number: {t['roll']}")
    print(f"Year: {t.get('Year')}")
    print(f"Branch: {t['branch']}")
    print(f"Total Marks: {sum(marks)}") 
    return 