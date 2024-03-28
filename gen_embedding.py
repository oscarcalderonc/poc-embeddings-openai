from client.openai_client import client
import os
import json
import hashlib

EMBEDDING_MODEL = os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
root_path = os.path.dirname(os.path.abspath(__file__))

def gen_embedding(
    inputPrompt: str,
):
    return client.embeddings.create(
        model=EMBEDDING_MODEL, input=inputPrompt, encoding_format="float"
    ).data[0].embedding

def load_embedding(file_name):
    prompts_folder = "prompts"
    hash_file_path = os.path.join(os.getcwd(), prompts_folder, file_name + "_hash.txt")
    no_hash_or_no_hash_match = False
    try:
        with open(hash_file_path, "r") as file:
            stored_hash = file.read()
            current_hash = generate_hash(file_name)
            if current_hash != stored_hash:
                print("business rules haven changed, generating a new embedding...")
                no_hash_or_no_hash_match = True
            else:
                print("business rules haven't changed, skipping embedding generation.")
            
    except FileNotFoundError:
        print(f"Error: Hash file '{file_name}' not found in the 'prompts' folder.")
        no_hash_or_no_hash_match = True
        
    if no_hash_or_no_hash_match == True:
        generate_and_save_hash(file_name)
        the_prompt = read_prompts_file(file_name)
        result = gen_embedding(the_prompt)
        save_embedding(file_name, the_prompt, result)
        

def read_prompts_file(file_name):
    prompts_folder = "prompts"
    file_path = os.path.join(os.getcwd(), prompts_folder, file_name + ".txt")
    
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(file_path)
        print(f"read_prompts_file Error: File '{file_name}' not found in the 'prompts' folder.")
        return None

def generate_hash(file_name):
    prompts_folder = "prompts"
    file_path = os.path.join(os.getcwd(), prompts_folder, file_name + ".txt")
    
    try:
        with open(file_path, "rb") as file:
            content = file.read()
            return hashlib.sha256(content).hexdigest()
    except FileNotFoundError:
        print(f"generate_hash Error: File '{file_name}' not found in the 'prompts' folder.")
        return None

def generate_and_save_hash(file_name):
    prompts_folder = "prompts"
    hash_file_name = file_name.split('.')[0] + "_hash.txt"
    hash_file_path = os.path.join(os.getcwd(), prompts_folder, hash_file_name)
    
    try:
        hash_value = generate_hash(file_name)
        with open(hash_file_path, "w") as hash_file:
            hash_file.write(hash_value)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found in the 'prompts' folder.")

def save_embedding(file_name, text, embedding_data):
    embeddings_folder = "raw_embeddings"
    embedding_file_name = file_name.split('.')[0] + "_embedding.json"
    embedding_file_path = os.path.join(os.getcwd(), embeddings_folder, embedding_file_name)
    
    try:
        with open(embedding_file_path, "w") as embedding_file:
            data = {"text": text, "embedding": embedding_data}
            json.dump(data, embedding_file)
        
        print(f"embedding saved to '{embedding_file_name}'.")
    except FileNotFoundError:
        print(f"Error: File '{embedding_file_name}' not found in the '{embeddings_folder}' folder.")

