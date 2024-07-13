import random

def make_num():
        select_num=[]
        while(True):
              temp_list=[]
              temp=random.randint(1000,10000)
              for i in range(temp-1):
                     i+=1
                     if(temp%i==0 and i!=1):
                           temp_list.append(i)
              if(len(temp_list)!=0):
                     break 
    
   
        num1=random.choice(temp_list)
        num2=int(temp/num1)

        select_num=[temp,num1,num2]
        return select_num
                
