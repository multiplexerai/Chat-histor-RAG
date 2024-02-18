# README for RAG Chat History Summarization System

## Overview

This project introduces a novel approach to managing interactive chat sessions, particularly focusing on optimizing token usage in API calls to large language models (LLMs) such as OpenAI's GPT-3.5. The core innovation lies in the summarization of chat history to reduce token count, thereby minimizing API usage costs and improving performance. The system is designed to facilitate complex question decomposition, answer aggregation, and feedback collection in specialized domains, making it particularly useful for applications requiring detailed and nuanced interactions, such as technical support or educational tutoring.

## Features

- **Session Management**: Utilizes Redis for efficient session handling, allowing for the retrieval and storage of chat histories associated with unique session tokens.
- **Chat History Summarization**: Implements a novel summarization technique to condense chat history, ensuring that token usage in subsequent API calls is minimized without sacrificing the context or quality of interactions.
- **Feedback Logging**: Incorporates a feedback mechanism for users to provide input on the system's responses, facilitating continuous improvement and customization based on user interactions.

## How It Works

1. **Start Chat**: Users initiate a chat session, receiving a unique session token. Chat history is stored in Redis, keyed by this token.
2. **Send Message**: Users send messages or questions within their session. The system can handle both simple queries directly and complex questions by breaking them down into simpler components.
3. **Summarization**: Before making an API call to the LLM for generating responses, the chat history is summarized to keep the token count low. This is crucial for keeping API costs manageable and ensuring efficient processing.
4. **Feedback Collection**: Users can provide feedback on the system's responses. This feedback is logged for analysis and future improvements.

## Technical Setup

### Dependencies

- FastAPI: For creating the RESTful API.
- Redis: For session management and storing chat histories.
- Pinecone: For vector database functionalities, enabling efficient query handling.
- OpenAI: For accessing GPT-3.5 and other LLMs for text generation and processing.

### Configuration

1. **Environment Setup**: Ensure Python 3.8+ is installed. Set up a virtual environment and install the required packages from `requirements.txt`.

2. **API Keys**: Obtain and configure the necessary API keys for OpenAI, Pinecone, and Redis in a `keys.py` file or through environment variables.

3. **Running the Application**: Start the FastAPI server with `uvicorn main:app --reload`. Replace `main` with the name of your Python script if different.

## Novel Idea: Chat History Summarization

The chat history summarization technique is designed to address the challenge of token limitations in API calls to LLMs. As conversations progress, the token count for the entire chat history can quickly exceed the limits for a single API request, leading to increased costs and potential performance bottlenecks.

To mitigate this, the system implements a summarization step that condenses the chat history into a shorter form that retains the essential context and information necessary for generating relevant responses. This approach not only reduces the number of tokens required for each API call but also ensures that the conversation remains coherent and contextually relevant over time.

## Future Directions

- **Custom Summarization Models**: Explore the development of custom LLMs tailored for chat history summarization, potentially improving efficiency and accuracy.
- **Domain Specialization**: Adapt the system for specific domains by training on specialized datasets, enhancing the relevance and quality of responses.
- **User Experience Enhancements**: Implement advanced features such as sentiment analysis and personalization to further improve user interactions.

## Conclusion

This project presents an innovative solution to managing interactive chat sessions with LLMs, with a particular focus on optimizing token usage through chat history summarization. By addressing the challenges of cost, performance, and context retention, the system offers a promising approach for a wide range of applications requiring detailed and nuanced conversational capabilities.
