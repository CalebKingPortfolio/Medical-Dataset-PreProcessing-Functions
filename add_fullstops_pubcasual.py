import re

def add_fullstops_pubcasual(processed_qm_output_df):

  # copy of the dataframe
  unprocessed_fs_output_df = processed_qm_output_df

  # gets the original size of the dataset
  processed_fs_ds = len(unprocessed_fs_output_df)

  # gets the subset used
  pubmed_subset = unprocessed_fs_output_df['subset_source'] == 'medical_meadow_pubmed_causal'

  # strips the output
  unprocessed_fs_output_df.loc[pubmed_subset, 'output'] = unprocessed_fs_output_df.loc[pubmed_subset, 'output'].astype(str).str.strip()

  # counts how many  rows have no full stop at the end
  fs_count_unprocessed = unprocessed_fs_output_df.loc[pubmed_subset, 'output'].apply(lambda x: len(re.findall(r'(?<![\.\?])$', x))).sum()

  # makes another copy for the processed one
  processed_fs_output_df = unprocessed_fs_output_df

  # replaces the no full stop with a full stop
  processed_fs_output_df.loc[pubmed_subset, 'output'] = processed_fs_output_df.loc[pubmed_subset, 'output'].replace(r'(?<![\.\?])$', '.', regex=True)

  # counts how many  rows have no full stop at the end
  fs_count_processed = processed_fs_output_df.loc[pubmed_subset, 'output'].apply(lambda x: len(re.findall(r'(?<![\.\?])$', x))).sum()

  return(processed_fs_ds, fs_count_unprocessed, fs_count_processed, processed_fs_output_df)
