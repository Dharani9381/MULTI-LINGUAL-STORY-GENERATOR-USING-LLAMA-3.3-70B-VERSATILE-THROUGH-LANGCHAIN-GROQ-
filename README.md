# MULTI-LINGUAL-STORY-GENERATOR-USING-LLAMA-3.3-70B-VERSATILE-THROUGH-LANGCHAIN-GROQ:
The Multi-Lingual Story Generator Using Llama-3.3-70B-Versatile Through LangChain &amp; Groq is an  AI-powered  web  application developed using Streamlit that enables users to generate creative stories in multiple languages based on customizable inputs. The system integrates the Llama-3.3-70BVersatile large language model through LangChain and Groq to produce high-quality, context-aware 
stories. Users can specify the story language, tone, category, creativity level, grammar complexity, 
target audience, time period, story idea, character names, and desired story length through an 
interactive sidebar interface. A PromptTemplate dynamically combines all user preferences into a 
structured prompt that guides the language model during story generation. The application supports 
multiple languages such as English, Telugu, Hindi, Tamil, Urdu, Kannada, and Chinese, allowing users 
to create stories in their preferred language. Different storytelling styles including Friendly, Narrative, 
and Poet can be selected to influence the writing style. The generated stories can belong to various 
genres such as Horror, Thriller, Adventure, Fantasy, Comedy, Drama, Family, and Suspense. Session 
state management is used to efficiently store and reuse the model and prompt template, improving 
application performance. By leveraging prompt engineering techniques, the system ensures that the 
generated content aligns closely with user requirements. The application demonstrates the practical 
integration of Generative AI, Prompt Engineering, LangChain, Groq inference services, and Streamlitbased user interfaces to create a personalized multilingual story 


Algorithm: Multi Lingual Story Generator Using Llama-3.3-70B-Versatile Through LangChain & Groq


1. Start the Streamlit application and initialize the user interface. 
2. Check whether the LLM model object exists in Streamlit session state. 
3. Load the Llama-3.3-70B-Versatile model through LangChain and Groq if not already loaded. 
4. Check whether the PromptTemplate object exists in session state. 
5. Create a reusable PromptTemplate containing all story-generation instructions. 
6. Display language selection options in the sidebar. 
7. Collect the desired story tone from the user. 
8. Accept the story idea or plot description as input. 
9. Receive the required story length in terms of paragraphs. 
10. Obtain the preferred grammar complexity level from the user. 
11.Collect the plagiarism preference level for content originality. 
12. Accept the story category such as Horror, Fantasy, Thriller, or Comedy. 
13. Receive the character names to be included in the story. 
14.Collect the preferred time period such as Ancient, Modern, or Future. 
15. Obtain the creativity level required for story generation. 
16. Receive the target audience category for personalization. 
17. Wait for the user to click the Submit button. 
18. Format all collected inputs into a final prompt using PromptTemplate. 
19. Send the generated prompt to the Llama-3.3-70B-Versatile model through LangChain and Groq 
and display the generated multilingual story to the user. 
20. End the execution after presenting the generated story output.

HOW TO RUN THE APPLICATION


To run the Multi-Lingual Story Generator Using Llama-3.3-70B-Versatile Through LangChain & 
Groq, first install Python on your system and create a project folder containing the Streamlit 
application file. Install the required libraries using pip install streamlit langchain langchain-groq 
langchain-core. Obtain a valid Groq API key and replace the placeholder API key in the source code. 
Save the application code in a file such as app.py. Open a terminal or command prompt and navigate 
to the project directory. Execute the command streamlit run app.py to start the application. Streamlit 
will automatically launch a local web server and display a URL in the terminal. Open the provided URL 
in a web browser to access the application interface. Enter the desired story parameters such as 
language, tone, category, creativity level, audience, and story idea through the sidebar controls. 
Finally, click the Submit button to generate and display the multilingual story produced by the Llama3.3-70B-Versatile model through LangChain and Groq.
