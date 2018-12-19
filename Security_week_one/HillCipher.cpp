#include<iostream>
#include<string>
#include<math.h>
using namespace std;

int main()
{
    //this part fills Alpha with Alphabet  letters
	char Alpha[26];
	for (int i = 0; i < 26; i++)
	{
		Alpha[i] = 65 + i;
	}

	string plain, plain2 = "", cipher;
	double n;
	cin >> n;
	unsigned int m = sqrt(n);
	unsigned long long temp = 0;

	//this part initiates a "two-dimensions" dynamic array for key
	unsigned long long ** key = new unsigned long long*[m];
	for (int i = 0; i < m; i++)
	{
		key[i] = new unsigned long long[m];
	}

	//this part takes in and fills key matrix
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> key[i][j];
		}
	}

	cin >> plain;
	plain2 = plain;
	// This part replaces plain with plain ending with X's
	for (int i = 0; i < m-(plain.length()%m); i++)
	{
		plain2 = plain2 + 'X';
	}
	// This part encrypts plain to cipher using key
	unsigned int pln = 0, some = 0, i = 0;
	while (i<plain2.length()){
		for (int k = 0; k < m; k++)
		{
			for (int l = 0; l < m; l++)
			{
				temp += key[k][l] * (unsigned int(plain2[pln] - 65));
				pln++;
			}
			cipher=cipher+ Alpha[temp % 26];
			pln = pln - m;
			temp = 0;
			i++;
			some++;
			if (some == m)
			{
				some = 0;
				pln = pln + m;
			}
		}
	}

	cout << cipher << endl;
}
