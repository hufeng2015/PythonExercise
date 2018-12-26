import math;


def fahrenheit_converter(C):
    fahrenheit = C * 9 / 5 + 32;
    return str(fahrenheit) + '摄氏度';


print(fahrenheit_converter(35));


def g2kg(G):
    kg = G / 1000;
    return str(kg) + "千克";


print(g2kg(20011));


def qxb(a, b):
    c = math.sqrt(math.pow(a,2) + math.pow(b,2));
    return '{0}和{1}的第三边是{2}'.format(a,b,c);


print(qxb(5, 6));

print('  *',' * *',"* * * ",'  |   ',sep='\n');
