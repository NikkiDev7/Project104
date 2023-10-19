import pandas as pd
import plotly.express as px
import csv

#Graph
# graphData = pd.read_csv("SOCR-HeightWeight.csv")
# graph = px.scatter(graphData, x = "Height(Inches)", y = "Weight(Pounds)")
# graph.show()

with open("SOCR-HeightWeight.csv") as data:
    reader = csv.reader(data)
    file_data = list(reader)

file_data.pop(0)
new_data = []

length = len(file_data)
for i in range(length):
    height = file_data[i][1]
    new_data.append(float(height))

#Mean
total = len(new_data)
sum = 0
for i in new_data:
    sum = sum + i
    
mean = sum/total
print(f"Mean is {mean}")


#Median
new_data.sort()
if total % 2 == 0:
    median1 = float(new_data[total//2])
    median2 = float(new_data[(total//2) -1])
    median = (median1 + median2) / 2  
else:
    median = new_data[total//2]
print("Median is {}".format(median))

#Mode
def get_mode(sorted_data):
    data = Counter(sorted_data)
    mode_data_for_range = {
    "75-85": 0,
    "85-95": 0,
    "95-105": 0,
    "105-115": 0,
    "115-125": 0,
    "125-135": 0,
    "135-145": 0,
    "145-155": 0,
    "155-165": 0,
    "165-175": 0
    }
    for weight, occurence in data.items():
        if 75 weight < 85:
            mode_data_for_range["75-85"] + occurence
        elif 85 weight < 95:
            mode_data_for_range["85-95"] + occurence
        elif 95< weight < 105:
            mode_data_for_range["95-105"]+ occurence 
        elif 105 weight < 115:
            mode_data_for_range["105-115"] += occurence 
        elif 115 weight < 125:
            mode_data_for_range["115-125"] + occurence 
        elif 125 < weight < 135:
            mode_data_for_range["125-135"] += occurence 
        elif 135 < weight < 145:
            mode_data_for_range ["135-145"] + occurence 
        elif 145 < weight < 155:
            mode_data_for_range["145-155"] + occurence 
        elif 155<weight < 165:
            mode_data_for_range ["155-165"] + occurence 
        elif 165 < weight < 175:
        mode_data_for_range ["165-175"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
    if occurence> mode_occurence:
        mode_range, mode_occurence = [int (range.split("-")[0]), int (range.split("-")[1])], occurence mode = float((mode_range[0] + mode_range [1]) / 2)
    print("Mode is -> {mode:27}")









# # #----------------MODE------------------
# # from collections import Counter
# # mode_data = Counter(new_data)
# # mode_data_for_range = {
# #     "50-60":0,
# #     "60-70":0,
# #     "70-80":0
# # }

# # '''
# # niketh = {
# #     "job":"student",
# #     "location":"USA"
# # }

# # niketh["job"] = student
# # '''

# # for key,value in mode_data.items():
# #     if 50< float(key) <60:
# #        mode_data_for_range["50-60"] += value
# #     elif 60< float(key) <70:
# #        mode_data_for_range["60-70"] += value
# #     elif 70< float(key) <80:
# #        mode_data_for_range["70-80"] += value

        
# # mode_range = 0
# # mode_occuernce = 0
# # for i,occ in mode_data_for_range.items():
# #     if occ > mode_occuernce:
# #         mode_range, mode_occuernce = [int(i.split("-")[0]), int(i.split("-")[1])]

# # mode = float((mode_range[0] + mode_range[1])/2)
# # print(f' mode is {mode}')