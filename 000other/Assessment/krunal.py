import master
role = 0

while role != 3 : 
    print("""WELCOME TO TOPS QUIZE GAMING CHALLANGE
        
        Select your role : 
        -> quize master : (press 1)
        -> quize creacker : (press 2)
        -> Exit : (press 3)

        """)
    role = int(input("Enter your role : "))

    if role == 1:
        choice = 0
        while choice != 4 : 
            print("""
                WELCOME MASTER
                SHAKE YOUR BRAIN AND ADD SOME CHALLANGING QUESTIONS.
                                - : MENU : -
                1 : Add questions
                2 : View questions
                3 : Delete questions
                4 : Exit

            """)

            choice = int(input("which opration you want to perform : "))
            if choice == 1:
                master.addQuesions()
            elif choice ==2 :
                master.viewQuestions()
            elif choice ==3:
                master.deleteQuestions()
    else:
        pass
    

