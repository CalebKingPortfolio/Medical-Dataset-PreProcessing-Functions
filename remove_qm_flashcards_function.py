# import re library
import re

def remove_qm_flashcards_function(processed_duplicates_df):

  # creates another copy of the dataframe
  unprocessed_qm_output_df = processed_duplicates_df.copy()

  # gets the length of the unprocessed dataframe
  unprocessed_fs_ds = len(unprocessed_qm_output_df)

  # get the length of rows from the 'medical_meadow_medical_flashcards' subset
  unprocessed_qm_ds = (unprocessed_qm_output_df['subset_source'] == 'medical_meadow_medical_flashcards').sum()

  # sets the subset getting fixed
  flashcards_subset = unprocessed_qm_output_df['subset_source'] == 'medical_meadow_medical_flashcards' 

  # strips the output of subset medical_meadow_medical_flashcards
  unprocessed_qm_output_df.loc[flashcards_subset, 'output'] = unprocessed_qm_output_df.loc[flashcards_subset, 'output'].astype(str).str.strip()
  
  # gets the length of the subset with question marks (using \s* to catch hidden spaces)
  qm_count_unprocessed = unprocessed_qm_output_df[flashcards_subset]['output'].astype(str).apply(lambda x: len(re.findall(r'\?\s*$', x))).sum()

  # checks which output lines end in question marks 
  unprocessed_qm = unprocessed_qm_output_df[flashcards_subset]['output'].astype(str).str.contains(r'\?\s*$', regex=True)

  # gets the index value of the outputs ending in question marks
  question_mark_indices = unprocessed_qm_output_df[flashcards_subset][unprocessed_qm].index.tolist()

  # removes the output values ending in question marks
  processed_qm_output_df = unprocessed_qm_output_df.drop(index=question_mark_indices)

  # recalculates the count after dropping to verify it is now 0
  qm_count_processed = processed_qm_output_df[processed_qm_output_df['subset_source'] == 'medical_meadow_medical_flashcards']['output'].astype(str).apply(lambda x: len(re.findall(r'\?\s*$', x))).sum()

  # gets the original size of the dataset
  processed_qm_ds = (processed_qm_output_df['subset_source'] == 'medical_meadow_medical_flashcards').sum()

  # gets the length of the processed dataframe
  processed_fs_ds = len(processed_qm_output_df)
  
  # return the variables that are used inside this function
  return(unprocessed_fs_ds, processed_fs_ds, unprocessed_qm_ds, qm_count_unprocessed, qm_count_processed, processed_qm_ds, processed_qm_output_df)
