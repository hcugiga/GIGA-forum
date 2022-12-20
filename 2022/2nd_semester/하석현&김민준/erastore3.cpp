#include <iostream>
#include <vector>
#include <iostream>

using namespace std;

int main() 
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	bool visit[1001] = { false, };
	int cnt = 0; 
	for (int i = 2; i <= N; i++) 
  {
		if (visit[i] == true) continue;
		for (int j = i; j <= N; j += i) 
    {
			if (visit[j] == false) 
      {
				visit[j] = true;
				cnt++; 
				if (cnt == K) 
        {
					cout << j << "\n";
					return 0;
				}
			}
		}
	}

	return 0;
}