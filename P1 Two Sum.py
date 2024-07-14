arr=[1,2,3,4,5,6,7]
target=25
value_dict={}
for first_value in arr:
    other_value=target-first_value
    if other_value in arr and other_value not in value_dict:
        value_dict[first_value]=other_value

if len(value_dict)!=0:
    print(value_dict)
else:
    print("No value forms the target")
            
    
