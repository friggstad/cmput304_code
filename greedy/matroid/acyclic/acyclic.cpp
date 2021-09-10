#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric> // for iota()

using namespace std;

struct edge {
  int u, v, w;
  bool operator<(const edge& rhs) const { return w < rhs.w; }
};

int find(int v, vector<int>& uf) {
  if (uf[v] != v) uf[v] = find(uf[v], uf);
  return uf[v];
}

// returns true iff there was an actual merger (i.e. they were
// in different sets)
bool merge(int u, int v, vector<int>& uf) {
  u = find(u, uf);
  v = find(v, uf);
  if (u == v) return false;
  uf[u] = v;
  return true;
}

int main() {
  int n, m;
  cin >> n >> m;
  vector<edge> edges(m);
  for (edge& e : edges) cin >> e.u >> e.v >> e.w;

  sort(edges.begin(), edges.end());
  reverse(edges.begin(), edges.end());

  vector<int> uf(n+1);
  iota(uf.begin(), uf.end(), 0); // initializes with 0, 1, 2, 3, ...

  vector<edge> solution;
  long long tot = 0; // use 64-bit types to aggregate the costs since they could get big
  for (edge e : edges)
    if (merge(e.u, e.v, uf)) {
      tot += e.w;
      solution.push_back(e);
    }

  for (edge e : solution) cout << e.u << ", " << e.v << " - " << e.w << endl;
  cout << "Maximum acyclic subgraph value: " << tot << endl;

  return 0;
}
