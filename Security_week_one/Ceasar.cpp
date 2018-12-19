#include<iostream>
#include<string>
using namespace std;

int main()
{
	string plain, cipher;
	char Alpha[26];
	long long int key = 0;
	cin >> key >> plain;
	for (int i = 0; i < 26; i++)
	{
		Alpha[i] = 65 + i;
	}
	cipher = plain;
	for (int i = 0; i < plain.length(); i++)
	{
		for (int j = 0; j < 26; j++)
		{
			if (plain[i] == Alpha[j])
			{
				cipher[i] = Alpha[(j + key) % 26];
				continue;
			}
		}
	}
	cout << cipher<<endl;
}