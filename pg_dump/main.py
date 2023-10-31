import psycopg2
import time
import logging

from core.settings import get_config

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    if get_config().project.need_backup:
        logging.info('start pg_dump. Sleeping')
        time.sleep(15)
        conn = psycopg2.connect(
            database=get_config().postgres.database,
            user=get_config().postgres.user,
            host=get_config().postgres.host,
            password=get_config().postgres.password,
            port=get_config().postgres.port
        )

        with open('dump.sql', 'r') as f:
            query = f.read()
            cur = conn.cursor()
            cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        logging.info('End pg_dump.')
    else:
        logging.info('Skip pg_dump.')
