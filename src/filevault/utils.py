import os
from Crypto.Random import get_random_bytes

def secure_delete(file_path):
    """
    Overwrites a file with random data before deleting it.
    WARNING: This is a destructive operation.
    """
    try:
        # Get the size of the file
        file_size = os.path.getsize(file_path)

        # Open the file in binary write mode to overwrite it
        with open(file_path, 'wb') as f:
            # Write random bytes over the entire file
            random_data = get_random_bytes(file_size)
            f.write(random_data)

        # Now, delete the file from the filesystem
        os.remove(file_path)
        print(f"🧹 Securely deleted original file: {file_path}")
        return True

    except FileNotFoundError:
        print(f"Warning: Could not find file to delete: {file_path}")
        return False
    except Exception as e:
        print(f"❌ Error during secure delete of {file_path}: {e}")
        return False