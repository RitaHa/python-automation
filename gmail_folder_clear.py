import logging
from multiprocessing.pool import ThreadPool
from imapclient import IMAPClient

logging.basicConfig(format='%(asctime)s:%(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CustomException(Exception):
    pass


def clear_gmail_folder(email, password, folder, max_count=0):
    attempts_count = 10
    deleted_qty = 0

    while attempts_count > 0 and deleted_qty < max_count:
        try:
            client = IMAPClient('imap.googlemail.com', use_uid=True, ssl=True)
            client.login(email, password)
        except Exception as e:
            raise CustomException('Error during login for {0}'.format(email), e)
        logger.info(f'Login into {email} mail box')
        client.select_folder(folder)
        messages = client.search()
        number_messages = len(messages)
        logger.info(f'Number of messages before deleting for {email} is: {number_messages}')
        try:
            if max_count and max_count < number_messages:
                client.delete_messages(messages[0:max_count])
            else:
                client.delete_messages(messages)
            status, response = client.expunge()
            deleted_qty = 0 if len(response) == 0 else len(response) - 1
            logger.info(f'Number of deleted messages for {email} is: {deleted_qty}')
            if len(client.search()) == 0:
                client.logout()
                break
        except IMAPClient.AbortError as e:
            logging.info(str(e))
        attempts_count -= 1


def clear_all_gmail_boxes(accounts, folder, max_count=0):
    [accounts[i].extend([folder, max_count]) for i, account in enumerate(accounts)]
    num_threads = len(accounts)
    pool = ThreadPool(num_threads)
    pool.starmap(clear_gmail_folder, accounts)

