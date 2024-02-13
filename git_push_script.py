import os
import subprocess

def git_push = '/Users/abdeabd/Desktop/AI'



(folder_path, commit_message, remote_name='origin', branch_name='main'):
    """
    Pushes the given folder to the specified remote and branch on GitHub.
    
    :param folder_path: The path to the folder to push.
    :param commit_message: The commit message to use.
    :param remote_name: The name of the remote. Default is 'origin'.
    :param branch_name: The name of the branch. Default is 'main'.
    """
    # Navigate to the folder
    os.chdir(folder_path)
    
    # Initialize Git if not already done
    if not os.path.exists(os.path.join(folder_path, '.git')):
        subprocess.run(['git', 'init'], check=True)
    
    # Add all files in the folder to the staging area
    subprocess.run(['git', 'add', '.'], check=True)
    
    # Commit the changes
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    
    # Push the changes to the remote repository
    subprocess.run(['git', 'push', remote_name, branch_name], check=True)

# Example usage:
folder_to_push = '/path/to/your/folder'  # Replace with your folder path
commit_msg = 'Initial commit with my AI project folders'
git_push(folder_to_push, commit_msg)
