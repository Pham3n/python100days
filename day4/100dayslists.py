#List data type/ data structure

saprovinces = ["KZN", "LMP", "GP", "MP", "WC", "EC", "NC", "FS"]

print(type(saprovinces)) #type of saprovinces is list

print(type(saprovinces[1])) #type of each item in saprovinces is string

saprovinces[1] = "LM" #change second item in list to string LM

print(saprovinces[-7]) #count from end to the begining, where last item is 1.. first is 8

saprovinces.extend(["NW"])

print(saprovinces)