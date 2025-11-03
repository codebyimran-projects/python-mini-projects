print("Welcome to the Share Bill System!\n")

persons_names=[]
exp_names=[]
bills={}
persons=int(input("Enter number of persons: "))

exp=True

while persons>0:
    name=input("Enter person name: ")
    persons_names.append(name)
    persons-=1


while exp:
    expenses=input("\nEnter expenses name: ")
    exp_names.append(expenses)
    ask=input("Do you want to enter expense names? (yes/no): ").lower()
    if ask=='yes':
        exp=True
    else:
        exp=False

        if exp==False:
            for i in exp_names:
                amount=float(input(f"Enter amount for {i}: "))
                bills[i]=amount


            print("\nExpense Summary:")
            for expense, amount in bills.items():
                print(f"{expense}: ${amount:.2f}")  

            total_amount=sum(bills.values())
            print(f"\nTotal Amount: ${total_amount:.2f}")

            share=total_amount/len(persons_names)
            print(f"Each person should pay: ${share:.2f}")
            
            print("\nIndividual Shares:")
            for person in persons_names:
                print(f"{person}: ${share:.2f}")
                

