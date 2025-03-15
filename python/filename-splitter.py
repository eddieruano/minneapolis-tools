# This script renames files in a specified directory by removing everything before the last dash ('-') in the filename.
# It keeps the part after the last dash and the file extension intact.
# Usage: Update the directory path and run the script.

import os

def rename_files(directory):
    renaming_count = 0  # Initialize a counter for renamed files
    total_files = len(os.listdir(directory))  # Get the total number of files in the directory
    for filename in os.listdir(directory):
        if "-" in filename:
            # Find the last dash in the filename
            last_dash_index = filename.rfind("-")
            # Extract the part after the last dash and the file extension
            new_filename = filename[last_dash_index + 1 :]
            # Full path for old and new filenames
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_filename}'")
            renaming_count += 1  # Increment the counter for each renamed file
    print(f"Renamed {renaming_count} out of {total_files} files.")  # Print summary of renaming

# Function to validate the directory
def validate_directory(directory):
    """Check if the provided directory exists and is a directory."""
    return os.path.isdir(directory)

# Function to handle invalid directory cases
# This could be expanded to include logging or raising exceptions if needed.
def handle_invalid_directory(directory):
    """Handle the case where the directory is invalid."""
    print(f"Error: The directory '{directory}' does not exist or is not a directory.")
    return False

# Main function to execute the renaming process
if __name__ == "__main__":
    directory = input("Enter the directory path: ").strip()
    # Ensure the directory exists
    if not validate_directory(directory):
        if not handle_invalid_directory(directory):
            exit(1)  # Exit if the directory is invalid

    # Ask user what delimiter to use (currently hardcoded to '-')
    delimiter = '-'  # This can be modified to accept user input if needed
    delimiter = input(f"Enter the delimiter to split filenames (default is '{delimiter}'): ").strip() or delimiter
    print(f"Using delimiter: '{delimiter}'")

    # Call the function to rename files
    rename_files(directory)
    print("Renaming completed./n")  # Indicate completion of the renaming process
