# cmput304_code

Implementations of some algorithms from the lectures. Some test data in the form of plain-text files is available to test each implementation.

For example, with the "longest common subsequence" implementation you can test it using:
- python3 lcs_bottom_up.py < sample1.txt

Some implementations are in C++11 and can be compiled, say, with:
- g++ codefile.cpp -std=c++11 -O2 -o exename

and then run with
- ./exename < sample1.txt

Of course, you can specify the executable name (i.e. use something other than "exename")
