from mrjob.job import MRJob
from mrjob.step import MRStep

class Sort_the_Word_Frequency_in_a_Book(MRJob):
    def steps(self):
        return [MRStep(mapper=self.mapper_get_words, reducer=self.reducer_count_words), MRStep(mapper=self.mapper_make_counts_key, reducer=self.reducer_output_words)]
    
    def mapper_get_words(self, _, line):
        words = line.split()
        for word in words:
            yield word.lower(), 1 

    def reducer_count_words(self, key, values):
        yield key, sum(values)

    def mapper_make_counts_key(self, key, value):
        yield None, (int(value), key)
    
    def reducer_output_words(self, _, word_count_pairs):
        for count, key in sorted(word_count_pairs):
            yield key, count

if __name__ == '__main__':
    Sort_the_Word_Frequency_in_a_Book.run()
