from mrjob.job import MRJob
from mrjob.step import MRStep

class Sort_the_Total_Amount_Spent_by_Customer(MRJob):
    def steps(self):
        return [MRStep(mapper=self.mapper_get_amount, reducer=self.reducer_total_amount), MRStep(mapper=self.mapper_make_amounts_key, reducer=self.reducer_output_amounts)]
    
    def mapper_get_amount(self, _, line):
        (customer_id, product_id, amount) = line.split(',')
        yield customer_id, float(amount)

    def reducer_total_amount(self, key, values):
        yield key, sum(values)

    def mapper_make_amounts_key(self, key, value):
        yield None, (float(value), key)

    def reducer_output_amounts(self, _, amount_customer_pairs):
        for amount, key in sorted(amount_customer_pairs):
            yield key, amount

if __name__ == '__main__':
    Sort_the_Total_Amount_Spent_by_Customer.run()