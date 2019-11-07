# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:25:51 2019

@author: changyu
"""

class student:
    #construction 
    def __init__(self, name, matric_number,*args): #init 前后应是双下滑线而不是但下滑线
        self.name = name
        self.matric_number = matric_number
        self.course = {}
        for c in args:  #course写入dictionary,初始化分数为0
             self.course[c]=0
                         
    def PrintStudent(self):
        print('name of student:', self.name)
        print('mariculation number:', self.matric_number)
        print('Course registered:', self.course)
        
    def AddGradeToStudent(self,**kw):
        for k,w in kw.items():
            if k in self.course.keys(): #写入的key如果与构造函数中的dict中的key匹配，在原字典中添加key，value对
                self.course[k]=w
            else:
                print('you didnt registered in the course %s'%(k))
                
            
student1 = student('tom',12345,'math','sport','computer')
student1.AddGradeToStudent(math=15, sport=20, chinese=100,english=50)
student1.PrintStudent()
        
        

        
        
        
        
        
        
        