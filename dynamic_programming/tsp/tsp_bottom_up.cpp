// bottom-up implementation of TSP in C++11

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<vector<int>> d(n, vector<int>(n));

  // if you want bigger, it will be really slow and you
  // should switch to 64-bit integer types to represent the set
  assert(n < 31);

  int INF = 0;
  for (auto& row : d)
    for (int& x : row) {
      cin >> x;
      INF = max(INF, (n+1)*x);
    }

  vector<vector<int>> memo((1 << n), vector<int>(n));
  auto backtrace = memo; // will create a copy

  for (int S = 0; S < (1 << n); ++S)
    if (S&1)
      for (int v = 1; v < n; ++v)
        if ((S>>v)&1) { // if we pass this, then we know S contains 0 and v
          if (S == 1+(1<<v)) { // if S represents {0,v}, base case
            memo[S][v] = d[0][v];
            backtrace[S][v] = 0;
          }
          else {
            memo[S][v] = INF;
            for (int u = 1; u < n; ++u)
              if (((S>>u)&1) && u != v) {
                int val = memo[S^(1<<v)][u] + d[u][v];
                if (val < memo[S][v]) {
                  memo[S][v] = val;
                  backtrace[S][v] = u;
                }
              }
          }
        }

  int S = (1<<n)-1, v = 1;
  for (int u = 2; u < n; ++u)
    if (memo[S][u] + d[u][0] < memo[S][v] + d[v][0])
      v = u;
  vector<int> answer(1, v);
  cout << "TSP Cost: " << memo[S][v] + d[v][0] << endl;
  while (S != 1) {
    int u = backtrace[S][v];
    answer.push_back(u);
    S = S^(1<<v);
    v = u;
  }

  reverse(answer.begin(), answer.end());
  for (int i : answer) cout << i << ' ';
  cout << endl;

  return 0;
}
