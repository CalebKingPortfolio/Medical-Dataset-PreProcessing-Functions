# import re library since wasn't working outside
import re

def remove_extra_spaces_function(processed_duplicates_df):

  # gives the dataframe another name
  unprocessed_spaces_df = processed_duplicates_df

  # SPACES AT START AND END

  # count number of cells with extra spaces at the start or end
  leading_trailing_spaces_unprocessed = unprocessed_spaces_df.apply(lambda col: col.astype(str).str.contains(r'^\s+|\s+$',na=False)).sum().sum()

  # removes extra spaces at the begining and end
  unprocessed_spaces_df[unprocessed_spaces_df.columns] = unprocessed_spaces_df.apply(lambda x: x.str.strip())

  # count number of cells with extra spaces at the start or end
  leading_trailing_spaces_processed = unprocessed_spaces_df.apply(lambda col: col.astype(str).str.contains(r'^\s+|\s+$',na=False)).sum().sum()

  # SPACES IN MIDDLE 

  # count total number of extra spaces
  unprocessed_total_matches = unprocessed_spaces_df.apply(lambda col: col.astype(str).apply(lambda x: sum(len(m) - 1 for m in re.findall(r'[ ]{2,}', x)))).sum().sum()

  # removes the extra spaces except extra lines
  processed_spaces_df = unprocessed_spaces_df.astype(str).replace(r'[ \t]+', ' ', regex=True)
  
  # count total number of extra spaces
  processed_total_matches = processed_spaces_df.apply(lambda col: col.astype(str).apply(lambda x: sum(len(m) - 1 for m in re.findall(r'[ ]{2,}', x)))).sum().sum()

  # gets the size of the dataset
  extra_spaces_ds = len(processed_spaces_df)
  
  # returns variables used within the function
  return(leading_trailing_spaces_unprocessed,leading_trailing_spaces_processed,unprocessed_total_matches,processed_total_matches, extra_spaces_ds, processed_spaces_df)
