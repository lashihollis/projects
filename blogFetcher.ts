/* Typescript Practice Challenge--with help from ChatGPT*/

// 1. Define a generic response wrapper
type ApiResponse<T> = {
  data: T;
  status: number;
};

// 2. Create a custom error class
class FetchError extends Error {
  constructor(message: string, public status: number) {
    super(message);
    this.name = "FetchError"; // name your error
  }
}

// 3. Define the generic fetch function
async function fetchBlogPost<T>(url: string): Promise<ApiResponse<T>> {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new FetchError("Failed to fetch blog post", response.status);
    }

    const data: T = await response.json();
    return { data, status: response.status };
  } catch (error) {
    if (error instanceof FetchError) {
      console.error(`FetchError: ${error.message} (Status: ${error.status})`);
    } else {
      console.error("Unexpected error:", error);
    }
    throw error;
  }
}

// 4. Define the BlogPost interface
interface BlogPost {
  id: number;
  title: string;
  body: string;
  author: string;
}

// 5. Call the function and handle the result
(async () => {
  try {
    const postResponse = await fetchBlogPost<BlogPost>("https://api.example.com/posts/1");

    const title = postResponse.data.title;
    const author = postResponse.data.author || "Unknown"; // fallback if empty

    console.log(`Blog Title: ${title}`);
    console.log(`Author: ${author}`);
  } catch (error) {
    console.log("Could not load blog post.");
  }
})();
