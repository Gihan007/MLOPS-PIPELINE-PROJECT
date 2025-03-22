import pickle

file_path = "models\model.pkl"  # Replace with your file path

# Load the Pickle file
with open(file_path, "rb") as file:
    data = pickle.load(file)

# Print the contents
print(data)
