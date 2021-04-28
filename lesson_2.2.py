broken_sentense = ['в', '5', 'часов' , '17' , 'минут' , 'температура', 'воздуха', 'была' , '+5', 'градусов']
for i, v in enumerate(broken_sentense):
    if v.replace("+", "").replace("-", "").isdigit():
        if v.isdigit():
            broken_sentense[i] = f' "{int(v):02}" '
        else:
            broken_sentense[i] = f'"{int(v):02}"'
#print(broken_sentense)
print(" ".join(broken_sentense))