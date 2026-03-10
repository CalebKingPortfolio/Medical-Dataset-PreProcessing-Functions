# import re library since wasn't working outside
import re

def remove_qm_flashcards_function(processed_duplicates_df):

  # gives the dataframe another name
  unprocessed_qm_output_df = processed_duplicates_df

  # gets the original size of the dataset
  unprocessed_fs_ds = len(unprocessed_qm_output_df)

  # gets the subset  used
  unprocessed_qm_ds = (unprocessed_qm_output_df['subset_source'] == 'medical_meadow_medical_flashcards').sum()

  # the subset getting checked
  flashcards_subset = unprocessed_qm_output_df['subset_source'] == 'medical_meadow_medical_flashcards' 

  # strips the output
  unprocessed_qm_output_df.loc[flashcards_subset, 'output'] = unprocessed_qm_output_df.loc[flashcards_subset, 'output'].astype(str).str.strip()
  
  # gets the length of the subset with question marks (using \s* to catch hidden spaces)
  qm_count_unprocessed = unprocessed_qm_output_df[flashcards_subset]['output'].astype(str).apply(lambda x: len(re.findall(r'\?\s*$', x))).sum()

  # checks for which output lines end in question marks (updated regex to match the count logic)
  unprocessed_qm = unprocessed_qm_output_df[flashcards_subset]['output'].astype(str).str.contains(r'\?\s*$', regex=True)

  # gets the index value of the outputs ending in question marks
  question_mark_indices = unprocessed_qm_output_df[flashcards_subset][unprocessed_qm].index.tolist()

  # removes the output values ending in question marks
  processed_qm_output_df = unprocessed_qm_output_df.drop(index=question_mark_indices)

  # recalculates the count after dropping to verify it is now 0
  qm_count_processed = processed_qm_output_df[processed_qm_output_df['subset_source'] == 'medical_meadow_medical_flashcards']['output'].astype(str).apply(lambda x: len(re.findall(r'\?\s*$', x))).sum()

  # gets the original size of the dataset
  processed_qm_ds = (processed_qm_output_df['subset_source'] == 'medical_meadow_medical_flashcards').sum()

  return(unprocessed_fs_ds, unprocessed_qm_ds, qm_count_unprocessed, qm_count_processed, processed_qm_ds, processed_qm_output_df)
