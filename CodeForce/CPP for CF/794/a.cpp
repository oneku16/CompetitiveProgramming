#include<bits/stdc++.h>
// # define ll long long;
	
using namespace std;
const int N = 2 * 10e5;
long long n, t;


void solve(){

	cin >> n;
	vector<int> arr1(n);

	for (int i = 0; i < n; i++) cin >> arr1[i];
	
	sort(arr1.begin(), arr1.end());
	int arr2[n];
	int used[n];
	for (int i = 0; i < n; i += 2){
		arr2[i] = arr1[i];
		used[i] = 1;
	}
	for (int i = 0; i < n; i ++){
		if (used[i] == 0){
			arr2[i] = arr1[i];	
		}
		
	}
	for (int i = 0; i < n; i ++) cout << arr2[i] << " \n"[i == n - 1];



}

int main(){

	cin >> t;
	while(t--) solve();


	return 0;
}