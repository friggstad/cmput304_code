// Remember to compile with --std=c++11 (or greater) if your compiler's default
// version is earlier than C++11.
//
// This implementation shows how we don't necessarily need to store the
// chosen subproblem to actually reconstruct the answer, we can just do
// it outside of the function.

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Returns the length of the longest common subsequence of the length i prefix of seq1
// and the length j prefix of seq2.
int lcs(int i, int j, const vector<int>& seq1, const vector<int>& seq2, vector<vector<int>>& memo) {
  if (memo[i][j] == -1) {
    if (i == 0 || j == 0)  {
      memo[i][j] = 0;
    }
    else if (seq1[i-1] == seq2[j-1]) {
      memo[i][j] = 1 + lcs(i-1, j-1, seq1, seq2, memo);
    }
    else {
      memo[i][j] = max(lcs(i-1, j, seq1, seq2, memo), lcs(i, j-1, seq1, seq2, memo));
    }
  }
  return memo[i][j];
}

int main() {
  int n, m;
  cin >> n >> m;

  vector<int> seq1(n), seq2(m);
  for (int& x : seq1) cin >> x;
  for (int& y : seq2) cin >> y;

  // memo[i][j] = -1 signals we have not computed this value yet
  vector<vector<int>> memo(n+1, vector<int>(m+1, -1));

  // compute LCS and print it
  cout << "LCS Length: " << lcs(n, m, seq1, seq2, memo) << endl;

  // construct the answer by tracing back through the DP table
  vector<int> answer;
  int i = n, j = m;
  while (i > 0 && j > 0) {
    if (seq1[i-1] == seq2[j-1]) {
      answer.push_back(seq1[i-1]);
      --i;
      --j;
    }
    else if (lcs(i-1, j, seq1, seq2, memo) >= lcs(i, j-1, seq1, seq2, memo)) {
      --i;
    }
    else {
      --j;
    }
  }
  // and reverse it because we construct the answer in reverse order
  reverse(answer.begin(), answer.end()); // from <algorithm>

  for (int i = 0; i < answer.size(); ++i) {
    cout << answer[i];
    if (i+1 == answer.size()) cout << endl;
    else cout << ' ';
  }

  return 0;
}
