/*
  Sorts a given sequence of words in linear time in the total length of all words.

  Works even if there are duplicates in the input by keeping track of a string
  count (not just a boolean like in the lecture notes).
*/

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cassert>

using namespace std;

struct TrieNode {
  map<char, TrieNode*> ch;
  int cnt; // how many occurrences of this string appear in the dictionary

  TrieNode() : cnt(0) {} // initialize counts to 0

  ~TrieNode() {
    for (auto p : ch) delete p.second;
  }
};

// v: root node of a trie
// inserts string s into the trie
void insert(TrieNode* v, const string& s) {
  for (auto c : s) {
    if (v->ch.find(c) == v->ch.end()) v->ch[c] = new TrieNode;
    v = v->ch[c];
  }
  v->cnt++;
}

// confer with the lecture notes pseudocode
void recursive_sort(TrieNode* v, string& s, vector<string>& sorted) {
  // add the number of copies of this string that appear in the dictionary
  for (int i = 0; i < v->cnt; ++i) sorted.push_back(s);

  // will iterate in increasing ASCII value of the character since the maps
  // are ordered in C++
  for (auto p : v->ch) {
    s.push_back(p.first);
    recursive_sort(p.second, s, sorted);
    s.pop_back();
  }
}

int main() {
  cout << "Reading input" << endl;

  int n;
  cin >> n;

  // read in the dictionary
  vector<string> dict(n);
  for (string& s : dict) cin >> s;

  cout << "Building trie" << endl;

  // build the trie
  TrieNode* root = new TrieNode;
  for (const string& s : dict) insert(root, s);

  cout << "Processing trie to build sorted list" << endl;

  // process the trie to get the sorted list
  vector<string> sorted;
  string s;
  recursive_sort(root, s, sorted);

  cout << "Printing sorted list" << endl << endl;
  for (const string& s : sorted) cout << s << endl;
  cout << endl;

  cout << "Done! Now checking against simple sorting" << endl;

  vector<string> copy = dict;
  sort(copy.begin(), copy.end());
  assert(copy == sorted);

  cout << "Finished" << endl;

  delete root;
}
