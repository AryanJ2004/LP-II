#include<iostream>
using namespace std;

void selectionsort(int arr[],int n);

int main()
{
	int n;
	cout<< "Enter the size of array: ";
	cin>>n;

	int arr[n];
	cout<<"Enter the elements of the array: ";
	for(int i=0; i<n; i++)
	{
		cin>>arr[i];
	}

	selectionsort(arr,n);
	return 0;
}

void selectionsort(int arr[],int n)
{
	int i,j,min,temp;

	for(i=0; i<n-1; i++)
	{
		min=i;
		for(j=i+1; j<n; j++)
		{
			if(arr[j] < arr[min])
			{
				min=j;
			}
		}

		temp = arr[i];
		arr[i] = arr[min];
		arr[min] = temp;
	}

	for(int i=0; i<n; i++)
	{
		cout<<arr[i]<<"\t";
	}
	cout<<"\n";
}