import pandas as pd
import sys

# sqlite3 -header -csv -readonly -header snippets-dev.db '.schema snippets'

# sqlite> UPDATE snippets SET commit_hash = REPLACE(commit_hash, CHAR(10), '');
# sqlite> UPDATE snippets SET commit_hash = REPLACE(commit_hash, CHAR(13), '');
 
# Run with sqlite3
# sqlite> PRAGMA auto_vacuum = FULL;
# sqlite> VACUUM;
# It will reduce the OG size by 100MB

# python parquet.py from.csv to.parquet
# df = pd.read_csv(sys.argv[1])
# df.to_parquet(sys.argv[2])

# parquet python still uses snappy instead of gzip
# df = pd.read_parquet(sys.argv[1], engine='pyarrow')
# df.to_parquet(sys.argv[2], compression='gzip')

