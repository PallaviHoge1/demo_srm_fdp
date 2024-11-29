from transformers import pipeline

# Load the pre-trained BERT model for Question Answering
qa_pipeline = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

# Context: Provide a paragraph for the model to answer questions from
context = """
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines
that are programmed to think like humans and mimic their actions. AI has applications in
various fields, including healthcare, finance, robotics, and more. One of its branches,
machine learning, enables systems to learn and improve from experience without being
explicitly programmed.
"""
def qna(context, question):

    # Continuous Q&A loop
    while True:
        if question.lower() == "exit":
            print("Goodbye!")
            break

        # Use the pipeline to get the answer
        result = qa_pipeline(question=question, context=context)

        # Print the answer
        return result["answer"]