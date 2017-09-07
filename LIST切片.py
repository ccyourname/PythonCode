lt=list(range(10))
print(lt)
#切片 [start:end:steps]    start<=x<end
print(lt[3:6:])   #[3,4,5]
print(lt[4:-2:])  #[4,5,6,7,8]
print(lt[::2])    #{0,2,4,6,8]
#倒序
print(lt[::-1])   #[9,8,7,6,5,4,3,2,1,0]
print(lt[9:0:-1]) #[9,8,7,6,5,4,3,2,1]
print(lt[::-2])   #[9,7,5,3,1]
print(lt[9:0:-2]) #[9,7,5,3,1]
print(lt[6-1:3-1:-1])   #[3,4,5]
#生成器
gt=[0]*3
print(gt)
gt=[[1]*2 for i in range(4)]
print(gt)
gt[0][1]=2
print(gt)
gt=[i*i for i in range(4)]#i平方
print('i平方:',gt)
gt=[2*i for i in range(4)]#i平方
print('i平方:',gt)
