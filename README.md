# page_rank
The program is mainly concer with the calculation of page rank values for each of the page and then updating them.Initially the input for 
the program is the matrix which consists of the link between the nodes.Finally we obtain the page which is most important with help of the 
ranks which are assigned to them.The concept behind the implementation is as follows.

Intuitively, we can think of PageRank as a kind of “ﬂuid” that circulates through the network, passing from node to node across edges, 
and pooling at the nodes that are the most important. Speciﬁcally, PageRank is computed as follows.

• In a network with n nodes, we assign all nodes the same initial PageRank, set to be 1/n.
• We choose a number of steps k. 
• We then perform a sequence of k updates to the PageRank values, using the following rule for each update:

Basic PageRank Update Rule: Each page divides its current PageRank equally across its out-going links, and passes these equal shares to the
pages it points to. (If a page has no out-going links, it passes all its current PageRank to itself.) Each page updates its new PageRank to
be the sum of the shares it receives.
