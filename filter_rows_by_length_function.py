def filter_rows_by_length_function(processed_spaces_df):

  # minumin and maximum  row size
  min_total_chars = 50
  max_output_chars = 2000

  # copy of the dataframe
  unprocessed_filtered_df = processed_spaces_df

  # gets the original size of the dataset
  unprocessed_filtered_ds = len(unprocessed_filtered_df)

  # count length per row
  unprocessed_filtered_df['total_len'] = (
      processed_spaces_df['instruction'].astype(str).str.len() +
      processed_spaces_df['input'].astype(str).str.len() +
      processed_spaces_df['output'].astype(str).str.len()
  )

  # keep rows with total_len >= min and output length <= max
  unprocessed_filtered_df = unprocessed_filtered_df[
      (processed_spaces_df['total_len'] >= min_total_chars) &
      (processed_spaces_df['output'].astype(str).str.len() <= max_output_chars)
  ]

  # drops the column total_len
  processed_filtered_df = unprocessed_filtered_df.drop(columns=['total_len'])

  # gets the original size of the dataset
  processed_filtered_ds = len(processed_filtered_df)

  # total number of rows droped
  total_droped = unprocessed_filtered_ds - processed_filtered_ds
  
  return(unprocessed_filtered_ds, processed_filtered_ds, total_droped, processed_filtered_df)
