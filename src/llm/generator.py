from openai import OpenAI

class Generator:
    def __init__(self, model="gpt-4.1-mini"):
        self.client = OpenAI()
        self.model = model

    def generate(self, question, context_chunks):
        context = "\n\n".join(context_chunks)
        prompt = f"""
            Answer the question using only the context given below
            Context:{context}
            Question:{question}
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{'role':'user', 'content': prompt}])
        return response.choices[0].message.content
