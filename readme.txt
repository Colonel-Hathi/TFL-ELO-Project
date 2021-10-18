Elo-Project
Made for INFOMTFL 2021-2022 @ UU

Dependencies:
Python 3.7
Numpy 1.21.2

This code simulates an Elo-based rating system wherein students are answering questions.
It was made for the purpose of tracking 'rating-drift' in Elo-based systems. 

Student and question amounts are class variables.

the simulate(x, y) method can be called to simulate students answering questions.
This method takes two arguments: 
x is the amount of questions each student answers.
y is the method whereby questions are matched to students:
-1 is random matching.
0 is 'perfect' matching (the student always gets the closest question in rating)
Any other value is treated as a 'rating range' where students are matched with random questions that fall within the rating range.

MIT License

Copyright (c) 2021 Colonel-Hathi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.