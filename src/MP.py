from multiprocessing import Pool
def f(x):
	return x*x
def main():
	p = Pool(5)
	print p.map(f,[1,2,3,4,5])
if __name__=="__main__":
	main()
