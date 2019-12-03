import logging
import time
from common.config import DEFAULT_TABLE
from common.const import default_cache_dir
# from common.config import DATA_PATH as database_path
from encoder.encode import feature_extract
from preprocessor.vggnet import VGGNet
from diskcache import Cache
from indexer.index import milvus_client, create_table, insert_vectors, delete_table, search_vectors, create_index, count_table


def do_count(table_name):
    print("trying....")
    try:
        index_client = milvus_client()
        num = count_table(index_client, table_name=table_name)
        return num
    except Exception as e:
        logging.error(e)
        return "Error with {}".format(e)