from mrjob.job import MRJob
from mrjob.step import MRStep
from statistics import mean

class Average_Number_of_Friends_by_Age(MRJob):
    def steps(self):
        return [MRStep(mapper=self.mapper_get_ages, reducer=self.reducer_average_ages)]
    
    def mapper_get_ages(self, _, line):
        (id, name, age, friends) = line.split(',')
        yield age, int(friends)

    def reducer_average_ages(self, key, values):
        yield key, mean(values)

if __name__ == '__main__':
    Average_Number_of_Friends_by_Age.run()