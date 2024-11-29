# demo_srm_fdp

### Modules Used

- **Flask**: A lightweight WSGI web application framework in Python. It is used to create the web server and handle HTTP requests.
- **summarize.py**: This module contains the `summarize_document` function, which is responsible for summarizing the uploaded document's content. You can enhance this function with more advanced summarization techniques as needed.

### Code Files

1. **app.py**: 
   - This is the main application file that sets up the Flask server and defines the routes for the application.
   - It includes the following routes:
     - `/`: The home route that renders the main interface for document upload.
     - `/upload`: Handles file uploads, reads the content of the uploaded document, and generates a summary using the `summarize_document` function.
     - `/ask`: Accepts user questions and provides answers based on the summary using the `answer_question` function.

2. **summarize.py**: 
   - Contains the `summarize_document` function, which currently provides a placeholder implementation for summarization. You can replace this with a more sophisticated summarization algorithm or library.

3. **templates/index.html**: 
   - The HTML template for the user interface. It includes a form for uploading documents, displays the generated summary, and allows users to ask questions based on the summary.

4. **data.txt**: 
   - A sample text file that can be used as input for the summarization function. It contains information about transformers in natural language processing.

## How to Run the Project

1. **Install Flask**: Make sure you have Flask installed. You can install it using pip:

   ```bash
   pip install Flask
   ```

2. **Run the Application**: Execute the following command in your terminal:

   ```bash
   python app.py
   ```

3. **Access the Application**: Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

4. **Upload a Document**: Use the provided interface to upload a text document (e.g., `data.txt`) and receive a summary.

5. **Ask Questions**: After viewing the summary, you can ask questions related to the content, and the application will provide answers based on the implemented logic.

## Future Enhancements

- Improve the summarization logic in `summarize.py` using advanced NLP techniques or libraries.
- Enhance the Q&A functionality to provide more accurate and context-aware answers.
- Implement user authentication and session management for a more personalized experience.

## License

This project is open-source and available for modification and distribution. Feel free to contribute or use it as a base for your own projects!