land = 1
water = 0




worlds = [[0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,1,0],
          [0,0,0,1,0,0,0,0,0,1,0],
          [0,0,0,1,0,1,1,0,0,0,0],
          [0,0,0,0,1,1,1,1,0,0,0],
          [0,0,0,1,1,1,1,1,1,1,0],
          [0,0,0,1,1,1,1,1,1,0,0],
          [0,0,0,1,1,0,1,1,1,0,0],
          [0,0,0,0,0,0,1,1,0,0,0],
          [0,1,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0]]

#a =      ['0','0','0','0','0','0','0','0','0','0','0',
 #         '0','0','0','0','1','1','0','0','0','0','0',
    #      '0','0','0','0','0','0','0','0','1','1','0',
  #        '0','0','0','1','0','0','0','0','0','1','0',
   #       '0','0','0','1','0','1','1','0','0','0','0',
     #     '0','0','0','0','1','1','1','1','0','0','0',
    #    '0','0','0','1','1','1','1','1','1','1','0'
     #     '0','0','0','1','1','1','1','1','1','0','0',
      #    '0','0','0','1','1','0','1','1','1','0','0',
       #   '0','0','0','0','0','0','1','1','0','0','0',
        #  '0','1','0','0','0','1','0','0','0','0','0',
         # '0','0','0','0','0','0','0','0','0','0','0']
#print (a.count('1'))

def continent_size(x,y):
   if worlds[x][y] == 1:
               print("land")
   else:
              print("water")
continent_size(5,5)

for y in range(len(worlds)):
                 print("\n")
                 for x in range(len(worlds[y] )):
                              
                              print (worlds[y][x], end='')
count=0
for x in range(len(worlds)):
    for y in range(len(worlds[x])):
                        
                if worlds[x][y] == 1:
                           
                            count=count + 1
                else:
                       pass
print('\n')                    
print("number of lands tile:",count)                    
               
           
      
              
