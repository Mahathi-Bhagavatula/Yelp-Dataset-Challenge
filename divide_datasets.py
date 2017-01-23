import pandas as pd
import json
import cPickle

values = open('/Users/mahathibhagavatula/Downloads/yelp_dataset_challenge_academic_dataset (1)/yelp_academic_dataset_review.json').read()

v = values.encode('utf-8')

# Can be any number based on number of reviews needed
short_v = v[:5000000]

subset_reviews = short_v.split("\n")

review_info =[]
counter=0
for each_split in subset_reviews:
    counter+=1
    if counter%100==0:
        print counter
    review_info.append(json.loads(each_split))

cPickle.dump(review_info, open("/Users/mahathibhagavatula/Downloads/yelp_data_subset.pkl","wb"))
