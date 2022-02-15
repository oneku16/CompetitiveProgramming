#include<bits/stdc++.h>


using namespace std;
const int N = 10e5 + 5;

int n, t, nums[N];


int main(){
    
    cin >> t;
    for (int k = 0; k < t; k++){
        cin >> n;
        for(int i=1; i<=n; i++){
            cin >> nums[i];
        }
        string ans = "YES";
        int i = 0;
        while (true){
            if (i == n)break;
            else{
                
                if (nums[i] > nums[i + 1]){
                    if ((nums[i] + nums[i + 1]) % 2 != 0){
                        swap(nums[i], nums[i + 1]);
                        i++;
                    }
                    else{
                        ans = "NO";
                        break;
                    }
                }
                else i++;
            }
        }
        cout << ans << endl;
    }
    
    

    return 0;
}