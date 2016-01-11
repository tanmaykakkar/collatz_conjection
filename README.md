# collatz_conjection

A gevent stream server, serving maximum cycle count among all collatz sequences for n in range of start-end, provided by user.

To run server:
# python streamserver.py
2016-01-12 02:31:46,187 Starting collatz maximum cycle count server on port 16000
2016-01-12 02:31:47,806 New connection from 127.0.0.1:33195

To make request:
1. Using telnet-
# telnet localhost 16000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Welcome to the collatz maximum cycle count server! Type quit to exit.
send range in format: start-end.
1-10000
collatz maximum cycle count is [262] for range 1-10000

2. Using netcat- 
# echo '1-1000000'| netcat localhost 16000
Welcome to the collatz maximum cycle count server! Type quit to exit.
send range in format: start-end.

Collatz conjecture states that for any number n, the below function f(n) will always boil down to 1, if you apply the same function over and over again to the previous result.

f(n) = {   
3n+1, if n is odd,  
n/2, if n is even  
1, if n is 1  
}  

Eg: if n = 20, then:  
f(20) = 20/2 = 10  
f(10) = 10/2 = 5  
f(5)  = 3*5+1 = 16  
f(16) = 16/2 = 8  
f(8)  = 8/2 = 4  
f(4)  = 4/2 = 2  
f(2)  = 1  

The term cycle count refers to the length of the sequence of numbers generated. In the above case, cycle count for f(20) is 8.  

The problem is as follows:  
Given a range of inputs (like 1-100), calculate the maximum cycle count that is encountered. As you can imagine, there is a lot of computation that is involved, for each number in the range. So optimise your logic with every method, you can think of.  

Your expected input range should be: 1 - 1million.  

Please use gevent (http://www.gevent.org/) [Github: https://github.com/surfly/gevent] to write a python server application that solves the 3n+1 problem.   
