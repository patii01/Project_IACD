from mrjob.job import MRJob
from mrjob.step import MRStep

class Minimum_Temperature_Per_Capital(MRJob):
    def self(self):
        return [MRStep(mapper=self.mapper_get_temp, reducer=self.reducer_min_temp)]
    
    def mapper_get_temp(self, _, line):
        (weather_station, date, observation, temp, _, _, _,) = line.split(',')
        if(observation == "TMIN"):
            yield weather_station, int(temp)

    def reducer_min_temp(self, key, values):
        yield key, min(values)

if __name__ == '__main__':
    Minimum_Temperature_Per_Capital.run()