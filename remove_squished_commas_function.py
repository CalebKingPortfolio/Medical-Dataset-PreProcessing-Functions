# import re library since wasn't working outside
import re

def remove_squished_commas_function(processed_spaces_df):

  # gives the dataframe another name
  unprocessed_commas_df = processed_spaces_df

  ## APPLIED

  # count total number of squished commas
  instruction_squished_commas_unprocessed = unprocessed_commas_df['instruction'].astype(str).apply(lambda x: len(re.findall(r',(?!\s)(?!\d)(?=.*\w)', x))).sum()
  input_squished_commas_unprocessed = unprocessed_commas_df['input'].astype(str).apply(lambda x: len(re.findall(r',(?!\s)(?!\d)(?=.*\w)', x))).sum()
  output_squished_commas_unprocessed = unprocessed_commas_df['output'].astype(str).apply(lambda x: len(re.findall(r',(?!\s)(?!\d)(?=.*\w)', x))).sum()

  # remove squished commas
  processed_commas_df = unprocessed_commas_df.astype(str).replace(r',(?!\s)(?!\d)(?=.*\w)', ', ', regex=True)

  # count total number of squished commas 
  instruction_squished_commas_processed = processed_commas_df['instruction'].astype(str).apply(lambda x: len(re.findall(r',(?!\s)(?!\d)(?=.*\w)', x))).sum()
  input_squished_commas_processed = processed_commas_df['input'].astype(str).apply(lambda x: len(re.findall(r',(?!\s)(?!\d)(?=.*\w)', x))).sum()
  output_squished_commas_processed = processed_commas_df['output'].astype(str).apply(lambda x: len(re.findall(r',(?!\s)(?!\d)(?=.*\w)', x))).sum()

  # gets size of the dataset
  processed_commas_ds = len(processed_commas_df)

  # returns variables used within the function
  return(instruction_squished_commas_unprocessed, input_squished_commas_unprocessed, output_squished_commas_unprocessed, instruction_squished_commas_processed, input_squished_commas_processed, output_squished_commas_processed, processed_commas_ds, processed_commas_df)
