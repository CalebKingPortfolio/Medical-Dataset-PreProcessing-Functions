import re

def remove_extra_spaces_function(processed_duplicates_df):

  # gives the dataframe another name
  unprocessed_spaces_df = processed_duplicates_df.copy().astype(str)

  # SPACES AT START AND END

  # count number of cells with extra spaces at the start or end (using \s to catch newlines)
  leading_trailing_spaces_unprocessed = unprocessed_spaces_df.apply(lambda col: col.str.contains(r'^\s+|\s+$', na=False)).sum().sum()

  # removes extra spaces at the beginning and end (including newlines)
  unprocessed_spaces_df = unprocessed_spaces_df.replace(r'^\s+|\s+$', '', regex=True)
  unprocessed_spaces_df = unprocessed_spaces_df.applymap(lambda x: re.sub(r'[ \t]+$', '', x, flags=re.MULTILINE))

  # count number of cells with extra spaces at the start or end AFTER cleaning
  leading_trailing_spaces_processed = unprocessed_spaces_df.apply(lambda col: col.str.contains(r'^\s+|\s+$', na=False)).sum().sum()

  # SPACES IN MIDDLE 

  # count total number of extra spaces per column
  extra_spaces_instruction_unprocessed = unprocessed_spaces_df['instruction'].apply(lambda x: sum(len(m) - 1 for m in re.findall(r'[ ]{2,}', x))).sum()
  extra_spaces_input_unprocessed = unprocessed_spaces_df['input'].apply(lambda x: sum(len(m) - 1 for m in re.findall(r'[ ]{2,}', x))).sum()
  extra_spaces_output_unprocessed = unprocessed_spaces_df['output'].apply(lambda x: sum(len(m) - 1 for m in re.findall(r'[ ]{2,}', x))).sum()

  # removes the extra horizontal spaces (leaves \n\n alone)
  # We use the already-trimmed unprocessed_spaces_df here!
  processed_spaces_df = unprocessed_spaces_df.replace(r'[ \t]{2,}', ' ', regex=True)
  
  # count total number of extra spaces per column
  extra_spaces_instruction_processed = processed_spaces_df['instruction'].apply(lambda x: sum(len(m) - 1 for m in re.findall(r'[ ]{2,}', x))).sum()
  extra_spaces_input_processed = processed_spaces_df['input'].apply(lambda x: sum(len(m) - 1 for m in re.findall(r'[ ]{2,}', x))).sum()
  extra_spaces_output_processed = processed_spaces_df['output'].apply(lambda x: sum(len(m) - 1 for m in re.findall(r'[ ]{2,}', x))).sum()

  # gets the size of the dataset
  extra_spaces_ds = len(processed_spaces_df)
  
  # returns variables used within the function
  return(leading_trailing_spaces_unprocessed,
         leading_trailing_spaces_processed, 
         extra_spaces_instruction_unprocessed, 
         extra_spaces_input_unprocessed, 
         extra_spaces_output_unprocessed,
         extra_spaces_instruction_processed, 
         extra_spaces_input_processed, 
         extra_spaces_output_processed,
         extra_spaces_ds,
         processed_spaces_df)

(leading_trailing_spaces_unprocessed,leading_trailing_spaces_processed, extra_spaces_instruction_unprocessed, extra_spaces_input_unprocessed, extra_spaces_output_unprocessed,extra_spaces_instruction_processed, extra_spaces_input_processed, extra_spaces_output_processed,extra_spaces_ds,processed_spaces_df) = remove_extra_spaces_function(processed_duplicates_df)
