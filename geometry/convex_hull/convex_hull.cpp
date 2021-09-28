/*
  Convex hull algorithms. Both Jarvis' March (O(n * h)) and
  Graham's Scan (O(n log n)).

  Assumes all points are 32-bit signed integers, n >= 3,
  no 3 points are collinear, and no 2 points are identical.
*/

#include <iostream>
#include <vector>

using namespace std;

using ll = long long;


struct point {
  ll x, y;

  point operator-(const point& rhs) const { return {x-rhs.x, y-rhs.y}; }
  point operator+(const point& rhs) const { return {x+rhs.x, y+rhs.y}; }
  bool operator<(const point& rhs) const;
  bool operator==(const point& rhs) const { return x == rhs.x && y == rhs.y; }
  bool operator!=(const point& rhs) const { return !(*this == rhs); }
};

ll cross(const point& p, const point& q) {
  return p.x*q.y - p.y*q.x;
}

// CAUTION: this does not necessarily define a well ordering of all possible points
// but it will when it is used in the convex hull algorithms (i.e. all points
// will have angle about the origin being the range [t, t+pi) about the origin for some value t.)
//
bool point::operator<(const point& rhs) const {
  return cross(*this, rhs) > 0;
}

// takes O(n*h) time where n == pts.size(), h == hull.size()
void check_hull(const vector<point>& pts, const vector<point>& hull) {
  // are all hull points part of pts?
  for (point p : hull) {
    bool found = false;
    for (point q : pts)
      if (p == q) found = true;
    assert(found);
  }

  // (j,i) index pairs march around the hull (wraparound)
  // make sure consecutive points on the hull turn CCW about each other
  // point in the input set
  for (int i = 0, j = hull.size()-1; i < hull.size(); j = i++)
    for (point p : pts)
      assert(cross(hull[j]-p, hull[i]-p) >= 0);
}


// find index of bottom-most point, breaking ties by leftmost
int find_bottom(const vector<point>& pts) {
  int start = 0;
  for (int i = 1; i < pts.size(); ++i)
    if (pts[i].y < pts[start].y || (pts[i].y == pts[start].y && pts[i].x < pts[start].x))
      start = i;
  return start;
}

vector<point> jarvis_march(const vector<point>& pts) {
  int start = find_bottom(pts), n = pts.size();

  // find point with least angle from the axis to the right of the start point
  int nxt = 0;
  for (int i = 0; i < n; ++i)
    if (i != start && cross(pts[i]-pts[start], pts[nxt]-pts[start]) >= 0)
      nxt = i;

  vector<point> hull = {pts[start], pts[nxt]};
  while (true) {
    int i = 0;
    while (pts[i] == hull.back()) ++i;
    for (int j = 0; j < n; ++j)
      if (pts[j] != hull.back() && cross(pts[j] - hull.back(), pts[i] - hull.back()) > 0)
        i = j;
    if (pts[i] == hull[0]) return hull;
    hull.push_back(pts[i]);
  }
}

vector<point> graham_scan(const vector<point>& pts) {
  int start = find_bottom(pts), n = pts.size();

  // translate all points so pts[start] is at the origin
  // and sort them by angle about the origin
  vector<point> shift;
  for (int i = 0; i < n; ++i)
    if (i != start)
      shift.push_back(pts[i] - pts[start]);
  sort(shift.begin(), shift.end());

  // do the march
  vector<point> hull = {{0,0}, shift[0]};
  for (int i = 1; i < shift.size(); ++i) {
    while (cross(shift[i] - hull.back(), hull[hull.size()-2] - hull.back()) < 0)
      hull.pop_back();
    hull.push_back(shift[i]);
  }

  // translate them back to their original positions
  for (point& p : hull) p = p + pts[start];

  return hull;
}

int main() {
  int n;
  cin >> n;
  vector<point> pts(n);
  for (point& p : pts) cin >> p.x >> p.y;

  vector<point> hull_jarvis = jarvis_march(pts);
  vector<point> hull_graham = graham_scan(pts);

  for (auto p : hull_graham) cout << p.x << ' ' << p.y << endl;

  check_hull(pts, hull_jarvis);
  check_hull(pts, hull_graham);


  return 0;
}
