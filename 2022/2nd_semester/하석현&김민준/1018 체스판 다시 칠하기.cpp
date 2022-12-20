#include <bits/stdc++.h>
using namespace std;

bool chess[50][50];

int getNum(int y, int x) {
    int a1 = 0, a2 = 0;
    bool l, color;

    l = 0;
    for(int i = y; i < y + 8; i++)
    {
        color = l;
        for(int j = x; j < x + 8; j++)
        {
            if(chess[i][j] != color)
                a1 ++;
            color = !color;
        }
        l = !l;
    }
    
    l = 1;
    for(int i = y; i < y + 8; i++)
    {
        color = l;
        for(int j = x; j < x + 8; j++)
        {
            if(chess[i][j] != color)
                a2 ++;
            color = !color;
        }
        l = !l;
    }

    return min(a1, a2);
}

int main() {
    int ans = 99999;

    int n, m;
    cin >> n >> m;

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
        {
            char input;
            cin >> input;
            if(input == 'W') chess[i][j] = true;
            if(input == 'B') chess[i][j] = false;
        }

    for(int i = 0; i + 8 <= n; i++)
        for(int j = 0; j + 8 <= m; j++)
        {
            int temp = getNum(i, j);
            if(temp < ans) ans = temp;
        }

    cout << ans;
}