# ��� - �б⹮
# if(����):

# ����-1

#85�� �̻� PASS, FAIL

score = int(input("������ �Է��� �ּ��� : "))

if(score>=85):
    print("PASS")
else:
    print("FAIL")

#���ڿ��� ��, ��ġ�ǳ�?
activity = input("�� ���Ƹ� ����?:")

if(activity=="�����̻���ó��"):
    print("��, �ʵ� �ڻ��?")
else:
    print("..�׷�..")

#5000�̻� : �ƿ��� / 3000�̻� : �н� / 1000�̻� : �Ŷ�� / �Ф�: �����
money = int(input("�� �� �־�?"))

if(money>=5000):
    print("�ƿ��� ����")
elif(money>=3000):
    print("�н� ����")
elif(money>=1000):
    print("�Ŷ�� ����")
else:
    print("����� ����ƾ�")

#else if = elif