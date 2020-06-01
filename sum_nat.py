def sum_nat(s):
    v = list(range(1,10))
    sub_v = []
    temp = s

    if s>=0 and s<=45:
        for i in range(0,len(v)):
            temp = temp - v[i]
            if temp >=0:
                sub_v.append(v[i])
                if sum(v)== s:
                    break
            else:
                temp = temp + v[i]
                for j in range(0,len(v)):
                    temp = temp - v[j]
                    if temp >=0:
                        sub_v.append(v[j])
                        if sum(v)== s:
                            break
                    else:
                        temp = temp + v[j]
                        continue
        print(sum(sub_v))
        return sub_v
    else:
        return "Please enter a number between [0,30]"

print(sum_nat(46))