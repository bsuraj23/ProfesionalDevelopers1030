movies={"Bahubali","RRR","KGF","Salaar","Jawan","Pathaan","Animal"}
telugu={"Bahubali","RRR","Salaar","Hanuman","Mirchi"}
print(movies.intersection(telugu)) #gives the intersection of the 2 sets
print(movies.union(telugu)) #gives the union of the two sets
up=movies.update(telugu) #updates the movies set
print(movies.difference(telugu)) #only returns the elements in the set movies and not the common elements 
print(telugu.difference(movies)) #only returns the elements in the set telugu that are not present in movies
