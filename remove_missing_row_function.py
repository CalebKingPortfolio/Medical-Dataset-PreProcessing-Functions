def remove_missing_row_function(df):

    # gives the dataframe another name
    unprocessed_missing_df = df

    # gets the orginal size of the dataset
    unprocessed_missing_ds = len(unprocessed_missing_df)

    # finds empty or missing rows and gets there index (row number)
    empty_rows_unprocessed = unprocessed_missing_df.index[unprocessed_missing_df.isnull().any(axis=1) | unprocessed_missing_df.apply(lambda col: col.astype(str).str.strip().eq("")).any(axis=1)].tolist()

    # count empty rows per column in the unprocessed dataset
    empty_instruction_rows_unprocessed = (unprocessed_missing_df['instruction'].isnull() | unprocessed_missing_df['instruction'].astype(str).str.strip().eq("")).sum()
    empty_input_rows_unprocessed = (unprocessed_missing_df['input'].isnull() | unprocessed_missing_df['input'].astype(str).str.strip().eq("")).sum()
    empty_output_rows_unprocessed = (unprocessed_missing_df['output'].isnull() | unprocessed_missing_df['output'].astype(str).str.strip().eq("")).sum()

    # gets the size of the mssing rows found
    missing_row_count_unprocessed = len(empty_rows_unprocessed)

    # drops the empty or missing rows
    processed_missing_df = unprocessed_missing_df.drop(index=empty_rows_unprocessed)

    # gets the processed size of the dataset
    processed_missing_ds = len(processed_missing_df)

     # finds empty or missing rows and gets there index (row number)
    empty_rows_processed = processed_missing_df.index[ processed_missing_df.isnull().any(axis=1) | processed_missing_df.apply(lambda col: col.astype(str).str.strip().eq("")).any(axis=1)].tolist()

    # count empty rows per column in the unprocessed dataset
    empty_instruction_rows_processed = (processed_missing_df['instruction'].isnull() | processed_missing_df['instruction'].astype(str).str.strip().eq("")).sum()
    empty_input_rows_processed = (processed_missing_df['input'].isnull() | processed_missing_df['input'].astype(str).str.strip().eq("")).sum()
    empty_output_rows_processed = (processed_missing_df['output'].isnull() | processed_missing_df['output'].astype(str).str.strip().eq("")).sum()

    # gets the size of the mssing rows found
    missing_row_count_processed = len(empty_rows_processed)

    # returns variables used within the function
    return(unprocessed_missing_ds,
           empty_instruction_rows_unprocessed,
           empty_input_rows_unprocessed,
           empty_output_rows_unprocessed,
           missing_row_count_unprocessed,
           processed_missing_ds,
           empty_instruction_rows_processed,
           empty_input_rows_processed,
           empty_output_rows_processed,
           missing_row_count_processed,
           processed_missing_df)
