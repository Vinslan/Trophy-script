import os
import shutil


project_name = str(input("Project: "))

os.makedirs(project_name, exist_ok = True)

path = project_name

print("Enter only numbers.")
medals ={
    "Bronze": abs(int(input("Bronze: "))),
    "Silver": abs(int(input("Siler: "))),
    "Gold": abs(int(input("Gold: ")))
}

counter = 1

for medal, counte in medals.items():
    for _ in range(counte):
        filename = f"TROP{counter:03}.PNG"
        souce_path = os.path.join("Defoult", f"{medal}.png")
        destination_path = os.path.join(path , filename)
        shutil.copy2(souce_path, destination_path)
        counter += 1
        
destination_path_p = os.path.join(path, "TROP000.PNG")
destination_path_icon = os.path.join(path, "ICON0.PNG")
            
shutil.copy2("Defoult/icon.png", destination_path_icon)
shutil.copy2("Defoult/platinum.png", destination_path_p)
            
        
