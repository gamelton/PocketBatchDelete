PocketBatchDelete is a Python script that allows users to delete multiple saved items from their Pocket account in a batch. Instead of manually deleting bookmarks one by one, this tool streamlines the process, making it efficient for users with numerous items to manage.

# Features

• Batch deletion of saved items in Pocket.  
• User-friendly interaction via web browser for authentication.  
• Customizable query to find and delete specific items based on keywords or URLs.  

# Prerequisites

• Python 3.x installed on your machine.  
• A registered application on Pocket Developer Portal to obtain your consumer key.  

# Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/PocketBatchDelete.git
    ```
2. Navigate to the project directory:

    ```
    cd PocketBatchDelete
    ```
   
3. Install required packages:

    ```
    pip install requests
    ```
   
# Configuration

1. Open the `delete_pocket_items.py` script in a text editor.  
2. Replace `CONSUMER_KEY` with your actual consumer key obtained from the Pocket Developer Portal.  
3. Modify the `query` variable to match the items you want to delete (this can be a keyword or a URL).  

    ```
    query = "your_keyword_or_url"
    ```

# Usage

1. Run the script:

    ```
    python delete_pocket_items.py
    ```

2. The script will:

   • Obtain a request token.  
   • Open your default web browser for authentication.  
   • Get an access token after you confirm application access.  
   • Search for items matching your query and delete them.  

# Important Notes

• Backup your Pocket data before running the script, as deleted items cannot be recovered.  
• Ensure that you have the necessary permissions set for your Pocket application in the developer portal.  

# Disclaimer

Use this script at your own risk. The developer is not responsible for any data loss or issues that may arise from using this tool.
