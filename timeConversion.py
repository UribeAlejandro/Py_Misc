def timeConversion(s):
    #
    # Write your code here.
    #
    am_pm = s[-2::1].upper()
    h = h = int(s[0:2])
    m_s = s[2:len(s)-2]

    if am_pm == 'AM':
        if h == 12:
            h = '00'
        else:
            h = '0'+str(h)
    elif am_pm == 'PM':
        if h ==12:
            h = str(h)
        else:
            h = str(h+12)
    return h+m_s

print(timeConversion('04:59:59AM'))