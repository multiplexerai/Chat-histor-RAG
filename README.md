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
