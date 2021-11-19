from mrjob.job import MRJob  #importing library MapReduce Job - big data mapping

# Create a class called Bacon_count, which inherits, or takes properties, from the MRJob class. 
class Bacon_count(MRJob): 
    # Next, create a mapper()function that will take (self, _, line) as parameters. 
    # The mapper() function will assign the input to key-value pairs:
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1
    
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
   Bacon_count.run()