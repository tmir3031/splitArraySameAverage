# splitArraySameAverage
<br>
To solve this problem I needed 2 steps.
<br>
Step 1: Partitioning<br>
    I divide the array into 2 parts:<br>
    - first part B, with b - no of elements<br>
    - the second part C, with c - no of elements<br>
    => sum(B)/b=sum(C)/c (1)<br>
        => it is known that: sum(C) = (sum(A)-sum(B))/(n-b)<br>
        => replacing in (1): sum(B)*(n-b) = (sum(A)-sum(B))*b<br>
        => n*sum(B) - b *sum(B) = b*sum(A) - b*sum(B)<br>
        => sum(B) = b*sum(A)/n (2)<br>
    - the possible function returns true if it finds a b between 1 and n-1 for which b * sum (A) / n == 0,
     which means that there may be a possible partition, otherwise false<br>
<br>
Step 2: Dynamic programming
<br>
    - I Created a data structure that stores all possible sums in the array up to n // 2, half the array of<br>
    - for each amount I see if there is an index for which an integer value is obtained by replacing in formula (2)<br>
    - finally I check if the value obtained is found in the calculated amounts<br>

