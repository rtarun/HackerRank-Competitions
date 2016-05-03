
##Input file: https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt

##The training data file will consist of 100 lines, each with 2 comma-separated numbers. 
##The first number denotes the amount of time the laptop was charged and the second denotes the amount of time the battery 
##lasted. The input for each of the test cases will consist of exactly 1 number rounded to 2 decimal places. 
##For each input, output 1 number: the amount of time you predict his battery will last.





x = []
y = []
data = open('trainingdata.txt')
for line in data:
    xi, yi = map(float, line.split(','))
    if ( xi < 4):
        x.append(xi)
        y.append(yi)
data.close()

n = len(x)
x_avg = sum(x) / n
y_avg = sum(y) / n

numerator = 0
denominator = 0
for i in xrange(n):
    x_diff = x[i] - x_avg
    numerator += x_diff * (y[i] - y_avg)
    denominator += x_diff ** 2
b = (1.0 * numerator) / denominator
a = y_avg - b * x_avg
q = float(raw_input())
if (q<4):
    print (float(a+ b * q))
else:
    print 8
