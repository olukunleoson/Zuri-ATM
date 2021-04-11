class Budget:

    print('Zuri python budget')
    budget_type1 = int(input('select category: 1 (Food) 2 (Cloth) 3 (Entertainment) \n'))
    if(budget_type1 == 1):
        input('Deposit amount \n')
        print('Money deposited to Food')
    elif(budget_type1 == 2):
        input('Deposit amount \n')
        print('Money deposited to Cloth')
    elif(budget_type1 == 3):
        input('Deposit amount \n')
        print('Money deposited to Entertainment')
    else:
        print('Invalid option')
        
                    
                            
    budget_type2 = int(input('select category: 1 (Food) 2 (Cloth) 3 (Entertainment) \n'))
    if(budget_type2 == 1):
        input('Withdrawal amount \n')
        print('Withdrawal completed')
    elif(budget_type2 == 2):
        input('Withdrawal amount \n')
        print('Withdrawal completed')
    elif(budget_type2 == 3):
        input('Withdrawal amount \n')
        print('Withdrawal completed')
    else:
        print('Invalid option')
        

    budget_type3 = int(input('select category: 1 (Food) 2 (Cloth) 3 (Entertainment) \n'))
    if(budget_type3 == 1):
        input('Transfer amount \n')
        print('Money transfered to Food')
    elif(budget_type3 == 2):
        input('Transfer amount \n')
        print('Money transfered to Cloth')
    elif(budget_type3 == 3):
        input('Transfer amount \n')
        print('Money transfered to Entertainment')
    else:
        print('Invalid option')
        
                    
    budget_type4 = budget_type1+budget_type2+budget_type3
        
        






