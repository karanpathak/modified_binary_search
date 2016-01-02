def binary_search(arr,key):
	n=len(arr)
	if key<arr[0]:return -1
	if key>arr[n-1]:return n+1
	l=0;r=n-1
	while r-l>1:
		mid=(l+r)/2
		if arr[mid]==key:return mid
		if arr[mid]>key:r=mid-1
		else:l=mid+1
	if arr[l]==key:return l
	if arr[r]==key:return r
	
	#uncomment to get ceil of key i.e. closest element to key such that arr[i]>key
	#return r
	
	#uncomment to get ceil of key i.e. closest element to key such that arr[i]<key
	#return l
	
	return "key not found" 

if __name__=="__main__":
    arr=map(int,raw_input().split())
    key=input()
    print binary_search(arr,key)
