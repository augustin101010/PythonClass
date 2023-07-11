import random

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