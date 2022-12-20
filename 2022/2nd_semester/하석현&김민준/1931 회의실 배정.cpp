#include <bits/stdc++.h>
using namespace std;


int main() {
    int n;
    cin >> n;
    pair<int, int> a[n];
    for(int i = 0; i < n; i++)
    {
        cin >> a[i].first;
        cin >> a[i].second;
    }

    sort(a, a + n);

    int select = 0;
    int ans = 1;
    for(int i = 1; i < n; i++)
    {
        // 겹치는 부분이 있을 때
        if(a[select].second > a[i].first) {
            a[i].second < a[select].second ? select = i : select = select;
        }
        //겹치는 부분이 없을 때
        else {
            ans++;
            select = i;
        }
    }

    cout << ans;
}