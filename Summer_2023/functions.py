from random import random

areAllModular = lambda arr,m,r : ( (arr[0]%m==r and areAllEven(arr[:-1])) if len(arr) else True )
modularOnly   = lambda l,h,m,r : [ i for i in range(l,h) if (i%m)==r ]

def grade(key, problem):
    try:
        if key == "p1a":
            assert problem == modularOnly(0,135,2,1)
        if key == "p1b":
            assert problem == modularOnly(3,177,2,0)
        
        if key == 'p3a':
            ntest = 50
            correct = 0
            for i in range(ntest):
                # Generate some random numbers to test your function at
                num_1 = 33*random.random()
                num_2 = 33*random.random()
    
                if problem(num_1,num_2) == num_1**2-num_2**2:
                    correct+=1
            print(correct,"/",ntest,"tests passed")
            assert correct == ntest
            
        if key == 'p3b':
            ntest = 50
            correct = 0
            for i in range(ntest):
                # Generate some random numbers to test your function at
                num = int(33*random.random())
                
                if problem(num) == [ i for i in range(num) ]:
                    correct+=1
            print(correct,"/",ntest,"tests passed")
            assert correct == ntest
        
        if key == 'p3c':
            ntest = 50
            correct = 0
            for i in range(ntest):
                # Generate some random numbers to test your function at
                num = int(1233*random.random())
    
                if problem(num) == ( num%17==4 ):
                    correct+=1
            print(correct,"/",ntest,"tests passed")
            assert correct == ntest
            
    except:
        print("Incorrect!")
        return
    
    print("Correct!")
    
    
def grade2(key, problem):
    
    ntrials = 50
    randmax = 33
    count = 0
    
    if key == "hw2_p1a":
        sol = lambda num : [ i for i in arr if i%2 == 0 ]
        for _ in range(ntrials):
            arr = []
            nelem = int(randmax*random())
            for _ in range(nelem):
                arr.append(int(randmax*random()))
            if problem(arr) == sol(arr):
                count += 1
        print(count,"/",ntrials,"tests passed")
        
    if key == "hw2_p1b":
        sol = lambda arr : [ i for i in range(1,num+1) if num%i==0 ]
        for _ in range(ntrials):
            num = int(randmax**3*random())
            if problem(num) == sol(num):
                count += 1
        print(count,"/",ntrials,"tests passed")
        
    if key == "hw2_p1c":
        sol = lambda n1,n2,n3 : min(n1,n2,n3)
        for _ in range(ntrials):
            nums = [ int(randmax**3*random()) for i in range(3)]
            if problem(*nums) == sol(*nums):
                count += 1
        print(count,"/",ntrials,"tests passed")
    
    if key == "hw2_p2a":
        sol = lambda n1,n2,n3 : max(n1,n2,n3) - min(n1,n2,n3)
        for _ in range(ntrials):
            nums = [ int(randmax**3*random()) for i in range(3)]
            if problem(*nums) == sol(*nums):
                count += 1
        print(count,"/",ntrials,"tests passed")
    
    if key == "hw2_p2b":
        sol = lambda c,arr : sol(c+arr[0]%2,arr[1:]) if len(arr) else c
        for _ in range(ntrials):
            nelem = int(12*random())
            nums  = [ int(randmax**3*random()) for i in range(nelem)]
            if problem(nums) == sol(0,nums):
                count += 1
        print(count,"/",ntrials,"tests passed")
    
    if key == "hw2_p2c":
        sol = lambda p,n : p if n%3!=0 else sol(p+1,n/3)
        for _ in range(ntrials):
            num  =  int(randmax**3*random())
            if problem(num) == sol(0,num):
                count += 1
        print(count,"/",ntrials,"tests passed")
    
    
    
    if count != ntrials:
        print("Incorrect!")
    else:
        print("Correct!")