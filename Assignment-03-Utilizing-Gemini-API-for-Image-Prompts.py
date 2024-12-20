import google.generativeai as genai
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt


def analyze_local_image(api_key, image_path):
    """
    Analyze a local image using Gemini
    """
    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        # Load and display local image
        image = Image.open(image_path)

        # Display image
        plt.figure(figsize=(10, 8))
        plt.imshow(image)
        plt.title("Local Image Analysis")
        plt.axis("off")
        plt.show()

        # Get analysis from Gemini
        response = model.generate_content(
            [
                "Please describe this image in detail. Include: "
                "1. Main subjects/objects"
                "2. Colors and composition"
                "3. Any text or numbers visible"
                "4. Overall context and setting",
                image,
            ]
        )

        print("\nImage Analysis Results:")
        print("-" * 50)
        print(response.text)

    except Exception as e:
        print(f"Error processing local image: {e}")


def analyze_url_image(api_key, image_url):
    """
    Analyze an image from URL using Gemini
    """
    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        # Load image from URL
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        # Display image
        plt.figure(figsize=(10, 8))
        plt.imshow(image)
        plt.title("URL Image Analysis")
        plt.axis("off")
        plt.show()

        # Get analysis from Gemini
        response = model.generate_content(
            [
                "Please describe this image in detail. Include: "
                "1. Main subjects/objects"
                "2. Colors and composition",
                image,
            ]
        )

        print("\nImage Analysis Results:")
        print("-" * 50)
        print(response.text)

    except Exception as e:
        print(f"Error processing URL image: {e}")


# Usage example
def main():
    api_key = (
        "AIzaSyChawzna0i51r9gKLYlGvbHKlU4-SkuCzk"  # Replace with your API key sir
    )

    # Analyze local image
    print("Analyzing Local Image...")
    local_image_path = "asd.jpg"  # Add image path your sir
    analyze_local_image(api_key, local_image_path)

    print("\n" + "=" * 50 + "\n")

    # Analyze URL image
    print("Analyzing URL Image...")
    image_url = "https://w0.peakpx.com/wallpaper/1002/321/HD-wallpaper-in-search-of-darkness-poster-thumbnail.jpg"  # Replace with your image URL
    analyze_url_image(api_key, image_url)


if __name__ == "__main__":
    main()
