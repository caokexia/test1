name='jack'
height=170
print ('my nsme is '+name+', and i am '+str(height)+'cm tall')
print ('my nsme is %s, and i am %xcm tall'%(name,345))
a=[('jack',12000),('lalais',8000)]
fs='''
%-8s salary: %8d $
%-8s salary: %8d $
'''
print (fs %(a[0][0],a[0][1],a[1][0],a[1][1]))


print ('my name is {}'.format('lili'))