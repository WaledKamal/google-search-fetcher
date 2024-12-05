from googlesearch import search

def get_google_results(query, num_results=10):
    """
    Fetch websites and links related to the given query from Google.
    
    Parameters:
        query (str): Search query description.
        num_results (int): Number of search results to retrieve.

    Returns:
        list: A list of dictionaries containing titles and URLs.
    """
    results = []
    try:
        for result in search(query, num_results=num_results, lang="en"):
            results.append(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return results

# Example usage
if __name__ == "__main__":
    query = input("Enter a description for the search (e.g., learning english websites): ")
    num_results = int(input("How many results do you want to retrieve? "))
    
    websites = get_google_results(query, num_results)
    
    if websites:
        print("\nSearch Results:")
        for idx, website in enumerate(websites, 1):
            print(f"{idx}. {website}")
    else:
        print("No results found.")
