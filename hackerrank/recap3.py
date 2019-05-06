# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

p = [15,12,8,8,7,7,7,6,5,3]
h = [10,25,17,11,13,17,20,13,9,15]

p_sum = sum(p)
p_mean = p_sum/len(p)
h_sum = sum(h)
h_mean = h_sum/len(h)
cov = 0
var_x = 0
for i in range(len(p)):
    cov+=(p[i]-p_mean)*(h[i]-h_mean)
    var_x+=(p[i]-p_mean)**2
B1 = cov/var_x
B0 = h_mean - B1*p_mean

ans = B1*10 + B0
print(round(ans,1))
