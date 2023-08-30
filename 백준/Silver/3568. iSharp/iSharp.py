exp = input().split()

for i in range(len(exp)):
    exp[i] = exp[i].replace(',', '')
    exp[i] = exp[i].replace(';', '')

varname = []

for i in range(1, len(exp)):
    alpha = list(filter(str.isalpha, exp[i]))
    alpha =''.join(alpha)
    varname.append(alpha)

for i in range(1, len(exp)):
    exp[i] = exp[i].replace(varname[i - 1], '')
    exp[i] = exp[i][::-1]
    exp[i] = exp[i].replace('][', '[]')

for i in range(1, len(exp)):
    exp[i] = exp[0] + exp[i] + " " + varname[i - 1] + ";";

for ele in exp[1:]:
    print(ele)