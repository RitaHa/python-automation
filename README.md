# Gmail Folder Clearing Script

## Overview

This script provides a solution to clear a Gmail folder using an app password and the IMAPClient library. If you're not familiar with app passwords, you can create one by following the instructions provided by Google: [How to create and use app password](https://support.google.com/mail/answer/185833?hl=en).

While this script uses IMAPClient and app passwords as one option to clear a Gmail folder, it's worth noting that another approach is to utilize the Gmail API. The Gmail API offers a comprehensive set of features to interact with Gmail accounts programmatically. For more details on using the Gmail API to delete messages, refer to the official documentation: [Gmail API - Delete Messages](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete).

## Usage

### Clearing Gmail Folder with IMAPClient

1. Install the required library:

    ```bash
    pip install IMAPClient
    ```

2. Modify the script with your Gmail account details and app password.

3. Run the script to clear the specified Gmail folder.

### Using Multiple Gmail Accounts with ThreadPool

If you want to use this script for more than one Gmail account concurrently, you can leverage the `ThreadPool` module. Update the script to handle multiple accounts, and use `ThreadPool` to execute the clearing operation concurrently.

## Important Notes

- Ensure that you handle sensitive information, such as app passwords securely.
- Review the permissions associated with the app password to ensure they have the necessary access.
- Take caution while using any script that involves deleting emails to avoid unintended data loss.