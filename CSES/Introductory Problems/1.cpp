#include <bits/stdc++.h>

using namespace std;


long long n;

void solve(){

	if (n % 2) n = n * 3 + 1;
	else n /= 2;
}


int main(){

	cin >> n;
	
	while (true){
		cout << n << ' ';
		if (n == 1) break;
		solve();
	}
	return 0;
}