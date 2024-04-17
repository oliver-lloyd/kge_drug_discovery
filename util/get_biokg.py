import pandas as pd
from pykeen.datasets import BioKG


def id_to_name(df, e_index, r_index):
    df = df.copy()
    df[0] = [e_index[ent] for ent in df[0].values]
    df[1] = [r_index[rel] for rel in df[1].values]
    df[2] = [e_index[ent] for ent in df[2].values]
    return df


biokg = BioKG()

ent_indexer = biokg.entity_to_id
ent_indexer = ent_indexer | {ent_indexer[key]: key for key in ent_indexer}

rel_indexer = biokg.relation_to_id
rel_indexer = rel_indexer | {rel_indexer[key]: key for key in rel_indexer}

train_ids = pd.DataFrame(biokg.factory_dict['training'].mapped_triples)
valid_ids = pd.DataFrame(biokg.factory_dict['validation'].mapped_triples)
test_ids = pd.DataFrame(biokg.factory_dict['testing'].mapped_triples)

train = id_to_name(train_ids, ent_indexer, rel_indexer)
train.to_csv('../../kge/data/biokg/train.txt', header=None, sep='\t', index=False)

valid = id_to_name(valid_ids, ent_indexer, rel_indexer)
valid.to_csv('../../kge/data/biokg/valid.txt', header=None, sep='\t', index=False)

test = id_to_name(test_ids, ent_indexer, rel_indexer)
test.to_csv('../../kge/data/biokg/test.txt', header=None, sep='\t', index=False)
