tasks_list=[];

while True:
   
   if len(tasks_list)==0:
        print('LIST YOUR FIRST TASK:')
        tasks=input()
        tasks_list.append(tasks)

   else:

        print('ADD ANOTHER TASK:')
        tasks=input()
        tasks_list.append(tasks)

   print('IF YOU ARE FINISHED TYPE "YES" OTHERWISE TYPE "NO"')
   RES=input()
   if RES.upper()=='YES':
       break

# print('YOUR TASKS ARE:', ' , '.join(tasks_list)) -- another way without loop
print('YOUR TASKS ARE:')
for i in tasks_list:
    print('- ',i)



