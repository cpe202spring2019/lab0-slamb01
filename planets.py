def weight_on_planets():
   # write your code here
   earthWeight = input("What do you weigh on earth? ")
   earthWeight = float(earthWeight)
   marsWeight = earthWeight * 0.38 
   jupiterWeight = earthWeight * 2.34
   print("\nOn Mars you would weigh", marsWeight, 'pounds.\nOn Jupiter you would weigh', jupiterWeight, 'pounds.')
   
if __name__ == '__main__':
   weight_on_planets()