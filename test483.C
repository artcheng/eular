#include <iostream>
#include <map>
#include <vector>
using namespace std;

int lcm(int a, int b)
{
	int prod=a*b;
	int c;
	while (a!=0)
	{
		c=a;
		a=b%a;
		b=c;
	}
	
	return prod/b;
}

void printMap(map<int, double> m)
{
	map<int, double>::iterator it;
	for(it = m.begin(); it != m.end(); it++)
	{
		cout<<it->first<<"\t"<<it->second<<endl;
	}
	cout<<"---------------"<<endl;
}

int main()
{
	int N=20;
	
	vector< map<int, double> > listD(N);
	map<int, double> d1;
	d1[1] = 1.0;
	listD[0] = d1;

	//printMap(d1);
	map<int, double>::iterator it;

	for(int n=2; n<N+1; n++)
	{
		map<int, double> dk;
		dk.clear();
		dk[n]=1.0/n;
		for(int k=1; k<n; k++)
		{
			map<int, double> d = listD[n-k-1];
			for(it = d.begin(); it != d.end(); it++)
			{
				int newp=lcm(k, it->first);
				if (dk.find(newp) == dk.end())
				{
					dk[newp] = it->second/n;
				}
				else
				{
					dk[newp] = dk[newp]+it->second/n;
				}
				
			}
		}
		listD[n-1] = dk;
		cout<<n<<", "<<dk.size()<<endl;
	}

	//printMap(listD[N]);

	map<int, double> dn = listD[N-1];
	double a=0.0;
        for(it = dn.begin(); it != dn.end(); it++)
	{
		a = a+it->first*it->first*it->second;
	}

	cout<<N<<": "<<a<<endl;
	
}
