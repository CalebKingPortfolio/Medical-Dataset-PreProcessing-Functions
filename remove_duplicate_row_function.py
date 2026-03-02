def remove_duplicate_row_function(processed_missing_df):

  # gives the dataframe another name
  unprocessed_duplicates_df = processed_missing_df 

  # gets the original size of the dataset
  unprocessed_duplicates_ds = len(unprocessed_duplicates_df)

  # finds the duplicates and gets there index (row number)
  duplicated_rows_uprocessed = unprocessed_duplicates_df.index[unprocessed_duplicates_df.duplicated()].tolist()

  # gets the size of the duplcate rows found
  duplicates_unprocessed = len(duplicated_rows_uprocessed)

  # drops the duplcated rows
  processed_duplicates_df = unprocessed_duplicates_df.drop(index=duplicated_rows_uprocessed)

  # gets the processed size of the dataset
  processed_duplicates_ds = len(processed_duplicates_df)

  # finds the duplicates found and gets their index (row number)
  duplicated_rows_processed = processed_duplicates_df.index[processed_duplicates_df.duplicated()].tolist()

  # gets the size of the duplcate rows found
  duplicates_processed = len(duplicated_rows_processed)

  # returns variables used within the function
  return(unprocessed_duplicates_ds, duplicates_unprocessed, processed_duplicates_ds, duplicates_processed, processed_duplicates_df)
