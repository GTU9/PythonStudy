import random

#곱셈식의 결과값을 보고 고합 두 인자를 네가지 보기중 두가지를 골라 맞추는 게임
class selectNumberGame:
      def __init__(self):
            self.select_num=[]
            self.result=0
      
      #임의로 만든 곱셈식의 결과 값을 result에 저장, 나머지 곱해지는 두 값을 랜덤으로 정해 select_num에 [0]자리와 [1]자리에 저장 
      def make_num(self):
        
        while(True):
              temp_list=[]
              temp=random.randint(1000,10000)
              for i in range(temp-1):
                     i+=1
                     if(temp%i==0 and i!=1): #곱해지는 값중 1과 자기자신을 제외함
                           temp_list.append(i)
              if(len(temp_list)!=0):
                     break 
    
   
        num1=random.choice(temp_list)
        num2=int(temp/num1)

        self.select_num=[num1,num2]
        self.result=temp

      #게임에 오답으로 사용할 값을 n개 정하고 배열에 추가
      def make_list(self,select_num,n):
            for i in range(n):
                  num=random.randint(1,1000)
                  select_num.append(num)

            return select_num

      #게임에 사용자에게 보여줄 곱셈식을 출력하고, 곱할값을 갱신하여 출력
      def print_quiz(self,num1="_",num2="_", result=""):
            print(f"{num1} X {num2} = {result}")

      #게임의 정답 확인
      def check_quiz(self,num1,num2,result):
            if(num1*num2==result):
                  print("정답입니다.")

            else:
                  print("오답입니다.")

